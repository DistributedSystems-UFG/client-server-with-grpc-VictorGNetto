from concurrent import futures

import grpc
import ListService_pb2
import ListService_pb2_grpc

class ListServer(ListService_pb2_grpc.ListServiceServicer):
    service_list = []

    def List(self):
        list = ListService_pb2.ListData()
        for item in self.service_list:
            list.data.append(item)
        return list

    def ShowList(self, request, context):
        return self.List()
    
    def Append(self, request, context):
        self.service_list.append(request.data)
        return self.List()
    
    def Clear(self, request, context):
        self.service_list.clear()
        return self.List()
    
    def Copy(self, request, context):
        return self.List()
    
    def CountElements(self, request, context):
        count = self.service_list.count(request.data)
        return ListService_pb2.Count(count=count)
    
    def Extend(self, request, context):
        self.service_list.extend(request.data)
        return self.List()
    
    def IndexOfElement(self, request, context):
        index = self.service_list.index(request.data)
        return ListService_pb2.Index(index=index)
    
    def Insert(self, request, context):
        self.service_list.insert(request.index, request.data)
        return self.List()
    
    def Pop(self, request, context):
        self.service_list.pop(request.index)
        return self.List()
    
    def Remove(self, request, context):
        self.service_list.remove(request.data)
        return self.List()
    
    def Reverse(self, request, context):
        self.service_list.reverse()
        return self.List()
    
    def Sort(self, request, context):
        self.service_list.sort()
        return self.List()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ListService_pb2_grpc.add_ListServiceServicer_to_server(
        ListServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
