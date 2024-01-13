
import mainproto_pb2
import mainproto_pb2_grpc
import grpc
import time
import os
import shuffle_sort
from concurrent import futures
import random 

ReducerPort = random.randint(9000, 9500)

print(f"Reducer with port - {ReducerPort} Requesting to register...")
with grpc.insecure_channel('localhost:50051') as channel:
        stub = mainproto_pb2_grpc.masterFunctionStub(channel)
        text = mainproto_pb2.Text(data=f"r{ReducerPort}")
        response = stub.newServer(text)
print("Reducer Registered!")

numMappers = response.value
listreducers = []

def write_to_file(data, path):
    with open(path, "w") as f:
        f.write(data)

def reduce(word_list, reducer_port):
    final_data = ""
    for key, value in word_list.items():
        final_data += f"{key} {value}\n"
    output_path = f"./Outputs/Output-Reducer-{reducer_port}.txt"
    write_to_file(final_data, output_path)

    
def sendClose():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mainproto_pb2_grpc.masterFunctionStub(channel)
        text = mainproto_pb2.Text(data="x")
        print("send close")
        response = stub.newServer(text)
        print(response)

class mainprotoServicer(mainproto_pb2_grpc.reduceFunctionServicer):
    def reduce_word(self, request, context):
        print(f"Reducer | Key-Value Pairs Received: {request.data}")
        
        shuffle_sort.base.append(request.data)
        print(f"Reducer ({ReducerPort}) | Data Received: {request.data}")
        print(shuffle_sort.base[0])
        
        val1 = 1
        return mainproto_pb2.ReduceNumber(value=val1)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
mainproto_pb2_grpc.add_reduceFunctionServicer_to_server(mainprotoServicer(), server)

print('Reducer Started - ')
print(str(ReducerPort))
server.add_insecure_port('[::]:'+ str(ReducerPort))
server.start()
flag = True

while True:
    if len(shuffle_sort.base) == numMappers and flag:
        print(shuffle_sort.base)
        shuffld = shuffle_sort.shuffleSort()
        reduce(shuffld)
        flag = False
        print("\nReducer %s Done!\n" % ReducerPort)
        try:
            sendClose()
        except grpc.RpcError as e:
            print("Error sending close message:", e)
            break


    