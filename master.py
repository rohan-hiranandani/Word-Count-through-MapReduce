import mainproto_pb2_grpc
import mainproto_pb2
from concurrent import futures
import grpc
import os
import time

import signal
import subprocess

class mainprotoServicer(mainproto_pb2_grpc.masterFunctionServicer):
    
    def __init__(self):
        self.mappers = []
        self.reducers = []
        self.finish = []

    def newServer(self, request, context):
        print(" ")
        temp = request.data
        print(temp)
        response = mainproto_pb2.Number()

        actions = {
        'm': self.add_mapper,
        'r': self.add_reducer,
        'x': self.handle_exit,
        }

        action = actions.get(temp[0], self.handle_default)
        response.value = action(temp)

        return response

    def add_mapper(self, temp):
        print(" ")
        print("Added a Mapper")
        mapindex = temp.find('8')
        self.mappers.append(temp[mapindex:mapindex+4])
        return len(self.mappers)

    def add_reducer(self, temp):
        print(" ")
        print("Added a Reducer")
        reduceindex = temp.find('9')
        self.reducers.append(temp[reduceindex:reduceindex+4])
        return len(self.mappers)

    def handle_exit(self, temp):
        print("time for exit")
        self.finish.append(1)
        print(len(self.finish))
        return -1

    def handle_default(self, temp):
        return 0

        
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mainproto_pb2_grpc.add_masterFunctionServicer_to_server(mainprotoServicer(), server)
print('Starting main server')
server.add_insecure_port('[::]:50051')
server.start()
print('Server started successfully!')


setup, inputGot, outputGot, send2Map, numberMappers, numberReducers = False, False, False, False, 0, 0

while True:
        if setup== False:
            MapProcess = []  #to store mapper processes
            MapProcessStatus = []
            ReduceProcess = []  #to store reducer processes
            ReduceProcessStatus = []
            numberMappers = int(input("Enter Number of Mappers - "))
            numberReducers = int(input(" Enter Number of Reducers - "))
            
            red2snd = str(numberReducers)
            i = 0
            while i < numberMappers:
                MapProcess.append(subprocess.Popen(['python', 'mapper.py']))
                MapProcessStatus.append(1)
                #print(MapProcessStatus)
                i += 1

            i = 0
            while i < numberReducers:
                ReduceProcess.append(subprocess.Popen(['python', 'reducer.py']))
                ReduceProcessStatus.append(1)
                #print(ReduceProcessStatus)
                i += 1

            print("waiting for setup complete")
            time.sleep(5)
            print()
            print("\nSetup Complete\n")
            setup = True
            
        elif outputGot !=True:
            outputGot = True
        
        elif inputGot!=True:
            inputfiles = []
            inputGot = True
            
            print("\nINPUT")
            while True:
                temp = input("Enter Input File Location (press enter to stop): ")
                if not temp:
                    break
            inputfiles.append(temp)
           

        elif send2Map!=True:
            send2Map = True
            
            print("\n-SEND TO MAPPERS ")
            
            numberFiles = len(inputfiles)
            print(numberFiles)
            
            quotient = int(numberFiles/numberMappers)
            extra2 = numberFiles-numberMappers
            extra = numberFiles%numberMappers

            temp =""  
            # Concatenate the reducers' names into a single string separated by dollar sign
            reducers_str = "$".join(mainprotoServicer.reducers)
            temp = reducers_str + "$"
            # Concatenate the reducers' string and the separator into the final string
            red2snd = red2snd + temp + "|"
            # Assign the number of files to be processed by each mapper
            if extra <= 0:
                currNum = quotient
            else:
                currNum = 1 + quotient
                extra -= 1

            # Process each file group assigned to a mapper
            for i in range(numberMappers):
                # Concatenate the file names into a single string separated by spaces
                    filesforMap = " ".join([inputfiles[numberFiles-1] for x in range(currNum) 
                            if x != 0] + [inputfiles[numberFiles-1]])
                    numberFiles -= currNum
                
            channel = grpc.insecure_channel('localhost:'+mainprotoServicer.mappers[i])
            stub = mainproto_pb2_grpc.mapFunctionStub(channel)
            print()
            sendtomapper = red2snd+filesforMap
            response = stub.mapWord(mainproto_pb2.MapText(data = sendtomapper))
        
        elif (len(mainprotoServicer.finish)==numberReducers):
            print("\nALL Reducers Complete")
            print(" ")
            print("\n\nMain Server is Now Exiting...")
            
            for proc in MapProcess:
                os.kill(proc.pid, signal.SIGTERM)
            print("\n\nAll Mappers Shut Down")
            for proc in ReduceProcess:
                os.kill(proc.pid, signal.SIGTERM)
            print("\n\nAll Reducers Shut Down")
            
        else:
            time.sleep(5)    











