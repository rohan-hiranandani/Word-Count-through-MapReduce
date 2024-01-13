import os
import grpc
import time
from concurrent import futures
import input_splitter
import mainproto_pb2
import mainproto_pb2_grpc
import random 

MapperPort = random.randint(8000, 8500)
print("Mapper port - " + str(MapperPort) + " Requesting to register...")
with grpc.insecure_channel('localhost:50051') as channel:
    stub = mainproto_pb2_grpc.masterFunctionStub(channel)

response = stub.newServer(mainproto_pb2.Text(data="M"+str(MapperPort)))

base = []
reducers = []

def send_to_reducer(key_pairs):
    # get the number of reducers from the first element in the list `reducers`
    num_reducers = reducers[0]
    # divide reducers alphabetically based on the number of reducers
    jump = 26 // num_reducers + 1
    key_pairs = key_pairs.split(" ")
    reducer_data = ['' for _ in range(num_reducers)]

    # loop through each key-value pair
    for pair in key_pairs:
        # calculate the index of the reducer for the current pair
        idx = max(min((ord(pair[1]) - ord('a')) // jump, num_reducers - 1), 0)
        # append the pair to the string of the corresponding reducer
        reducer_data[idx] = reducer_data[idx] + " " + pair

    # loop through each reducer, except the first one, and send its data
    for i, reducer_port in enumerate(reducers[1:]):
        channel = grpc.insecure_channel('localhost:' + reducer_port)
        stub = mainproto_pb2_grpc.reduceFunctionStub(channel)
        response = stub.redWord(mainproto_pb2.ReduceText(data=reducer_data[i]))
        print("Reducer %s - %s" % (reducer_port, response.value))

    # print the data for all reducers
    print(reducer_data)

    
    
class mainprotoServicer(mainproto_pb2_grpc.mapFunctionServicer):
    def mapWord(self, request, context):
        print("MAPPER | Files Received")
        
        # Extract the number of reducers and reducer addresses
        num_reducers, *reducer_addrs, text = request.data.split('$')
        reducer_addrs = reducer_addrs[:int(num_reducers)]
        
        # Print reducer addresses and available reducers
        print("Reducer Addresses - ", reducer_addrs)
        print("Available Reducers - ", len(reducer_addrs))
        
        # If text is empty, send reduce requests and return
        if not text.strip():
            print("Mapper base")
            for addr in reducer_addrs:
                with grpc.insecure_channel(f'localhost:{addr}') as channel:
                    stub = mainproto_pb2_grpc.reduceFunctionStub(channel)
                    response = stub.redWord(mainproto_pb2.ReduceText(data=""))
                    print(f"Reducer {addr} - {response.value}")
            return mainproto_pb2.MapNumber(value=1)
        
        # Process the text in the given files
        files = text.split()
        print("Input Files -", files)
        combined_text = " ".join(open(file, 'r').read() for file in files)
        
        # Append the combined text to base
        base.append(combined_text)
        
        return mainproto_pb2.MapNumber(value=1)

 
with futures.ThreadPoolExecutor(max_workers=10) as executor:
    server = grpc.server(executor)
    mainproto_pb2_grpc.add_mapFunctionServicer_to_server(mainprotoServicer(), server)
    print('Mapper Started - ' + str(MapperPort))
    server.add_insecure_port('[::]:'+ str(MapperPort))
    server.start()
    server.wait_for_termination()

while True:
        if len(base)>0:
            temp = input_splitter.InputSplitter(base[0])
            print("input successfully split")
            base.pop(0)
            send_to_reducer(temp)
            print("successful sent to reducer")
        else:
            print("mapper error check mapper.py")
