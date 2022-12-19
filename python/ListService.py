from concurrent import futures

import grpc
import ListService_pb2
import ListService_pb2_grpc

class ListServer(ListService_pb2_grpc.ListServiceServicer):
    service_list = [1, 2, 3, 4]

    def ShowList(self, request, context):
        list = ListService_pb2.ListData()
        for item in self.service_list:
            list.data.append(item)
        return list

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ListService_pb2_grpc.add_ListServiceServicer_to_server(
        ListServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
