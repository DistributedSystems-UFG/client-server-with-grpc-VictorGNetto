import grpc
import ListService_pb2
import ListService_pb2_grpc

import const

def gRPC_to_list(gRPCdata):
    pass

def run():
    with grpc.insecure_channel(const.IP + ':' + const.PORT) as channel:
        stub = ListService_pb2_grpc.ListServiceStub(channel)

        res = stub.ShowList(ListService_pb2.EmptyMessage())
        print("ShowList: ", res.data)

if __name__ == '__main__':
    run()