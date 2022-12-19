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

        stub.Append(ListService_pb2.Data(data=6))
        stub.Append(ListService_pb2.Data(data=5))
        stub.Append(ListService_pb2.Data(data=6))
        res = stub.ShowList(ListService_pb2.EmptyMessage())
        print("Append: ", res.data)

        res = stub.Copy(ListService_pb2.EmptyMessage())
        print("Copy: ", res.data)

        res = stub.CountElements(ListService_pb2.Data(data=6))
        print("Count: ", res.count)

        listdata = ListService_pb2.ListData()
        listdata.data.extend([7, 7, 8, 9, 9, 9])
        res = stub.Extend(listdata)
        print("Extend: ", res.data)

        res = stub.IndexOfElement(ListService_pb2.Data(data=8))
        print("Index: ", res.index)

        res = stub.Insert(ListService_pb2.InsertData(index=1, data=5))
        print("Insert: ", res.data)

        res = stub.Pop(ListService_pb2.Index(index=1))
        print("Pop: ", res.data)

        res = stub.Remove(ListService_pb2.Data(data=8))
        print("Remove: ", res.data)

        res = stub.Reverse(ListService_pb2.EmptyMessage())
        print("Reverse: ", res.data)

        res = stub.Sort(ListService_pb2.EmptyMessage())
        print("Sort: ", res.data)

        res = stub.Clear(ListService_pb2.EmptyMessage())
        print("Clear: ", res.data)

if __name__ == '__main__':
    run()