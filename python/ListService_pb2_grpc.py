# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ListService_pb2 as ListService__pb2


class ListServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ShowList = channel.unary_unary(
                '/list_service.ListService/ShowList',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Append = channel.unary_unary(
                '/list_service.ListService/Append',
                request_serializer=ListService__pb2.Data.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Clear = channel.unary_unary(
                '/list_service.ListService/Clear',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Copy = channel.unary_unary(
                '/list_service.ListService/Copy',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.CountElements = channel.unary_unary(
                '/list_service.ListService/CountElements',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.Count.FromString,
                )
        self.Extend = channel.unary_unary(
                '/list_service.ListService/Extend',
                request_serializer=ListService__pb2.ListData.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.IndexOfElement = channel.unary_unary(
                '/list_service.ListService/IndexOfElement',
                request_serializer=ListService__pb2.Data.SerializeToString,
                response_deserializer=ListService__pb2.Index.FromString,
                )
        self.Insert = channel.unary_unary(
                '/list_service.ListService/Insert',
                request_serializer=ListService__pb2.InsertData.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Pop = channel.unary_unary(
                '/list_service.ListService/Pop',
                request_serializer=ListService__pb2.Index.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Remove = channel.unary_unary(
                '/list_service.ListService/Remove',
                request_serializer=ListService__pb2.Data.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Reverse = channel.unary_unary(
                '/list_service.ListService/Reverse',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )
        self.Sort = channel.unary_unary(
                '/list_service.ListService/Sort',
                request_serializer=ListService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ListService__pb2.ListData.FromString,
                )


class ListServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ShowList(self, request, context):
        """Show list values
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Append(self, request, context):
        """Ads an element at the end of the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Clear(self, request, context):
        """Removes all the elements from the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Copy(self, request, context):
        """Returns a copy of the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CountElements(self, request, context):
        """Returns the number of elements with the specified value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Extend(self, request, context):
        """Add the elements of a list (or any iterable), to the end of the current list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IndexOfElement(self, request, context):
        """Returns the index of the first element with the specified value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Insert(self, request, context):
        """Adds an element at the specified position
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pop(self, request, context):
        """Removes the element at the specified position
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Removes the first item with the specified value
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reverse(self, request, context):
        """Reverses the order of the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sort(self, request, context):
        """Sorts the list
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ListServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ShowList': grpc.unary_unary_rpc_method_handler(
                    servicer.ShowList,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Append': grpc.unary_unary_rpc_method_handler(
                    servicer.Append,
                    request_deserializer=ListService__pb2.Data.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Clear': grpc.unary_unary_rpc_method_handler(
                    servicer.Clear,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Copy': grpc.unary_unary_rpc_method_handler(
                    servicer.Copy,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'CountElements': grpc.unary_unary_rpc_method_handler(
                    servicer.CountElements,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.Count.SerializeToString,
            ),
            'Extend': grpc.unary_unary_rpc_method_handler(
                    servicer.Extend,
                    request_deserializer=ListService__pb2.ListData.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'IndexOfElement': grpc.unary_unary_rpc_method_handler(
                    servicer.IndexOfElement,
                    request_deserializer=ListService__pb2.Data.FromString,
                    response_serializer=ListService__pb2.Index.SerializeToString,
            ),
            'Insert': grpc.unary_unary_rpc_method_handler(
                    servicer.Insert,
                    request_deserializer=ListService__pb2.InsertData.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Pop': grpc.unary_unary_rpc_method_handler(
                    servicer.Pop,
                    request_deserializer=ListService__pb2.Index.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=ListService__pb2.Data.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Reverse': grpc.unary_unary_rpc_method_handler(
                    servicer.Reverse,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
            'Sort': grpc.unary_unary_rpc_method_handler(
                    servicer.Sort,
                    request_deserializer=ListService__pb2.EmptyMessage.FromString,
                    response_serializer=ListService__pb2.ListData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'list_service.ListService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ListService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ShowList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/ShowList',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Append(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Append',
            ListService__pb2.Data.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Clear(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Clear',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Copy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Copy',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CountElements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/CountElements',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.Count.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Extend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Extend',
            ListService__pb2.ListData.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IndexOfElement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/IndexOfElement',
            ListService__pb2.Data.SerializeToString,
            ListService__pb2.Index.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Insert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Insert',
            ListService__pb2.InsertData.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Pop',
            ListService__pb2.Index.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Remove',
            ListService__pb2.Data.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reverse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Reverse',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/list_service.ListService/Sort',
            ListService__pb2.EmptyMessage.SerializeToString,
            ListService__pb2.ListData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
