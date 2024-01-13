# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mainproto_pb2 as mainproto__pb2


class masterFunctionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.newServer = channel.unary_unary(
                '/masterFunction/newServer',
                request_serializer=mainproto__pb2.Text.SerializeToString,
                response_deserializer=mainproto__pb2.Number.FromString,
                )
        self.fetchServers = channel.unary_unary(
                '/masterFunction/fetchServers',
                request_serializer=mainproto__pb2.Text.SerializeToString,
                response_deserializer=mainproto__pb2.Text.FromString,
                )


class masterFunctionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def newServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fetchServers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_masterFunctionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'newServer': grpc.unary_unary_rpc_method_handler(
                    servicer.newServer,
                    request_deserializer=mainproto__pb2.Text.FromString,
                    response_serializer=mainproto__pb2.Number.SerializeToString,
            ),
            'fetchServers': grpc.unary_unary_rpc_method_handler(
                    servicer.fetchServers,
                    request_deserializer=mainproto__pb2.Text.FromString,
                    response_serializer=mainproto__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'masterFunction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class masterFunction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def newServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/masterFunction/newServer',
            mainproto__pb2.Text.SerializeToString,
            mainproto__pb2.Number.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def fetchServers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/masterFunction/fetchServers',
            mainproto__pb2.Text.SerializeToString,
            mainproto__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class mapFunctionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.mapWord = channel.unary_unary(
                '/mapFunction/mapWord',
                request_serializer=mainproto__pb2.MapText.SerializeToString,
                response_deserializer=mainproto__pb2.MapNumber.FromString,
                )


class mapFunctionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def mapWord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_mapFunctionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'mapWord': grpc.unary_unary_rpc_method_handler(
                    servicer.mapWord,
                    request_deserializer=mainproto__pb2.MapText.FromString,
                    response_serializer=mainproto__pb2.MapNumber.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mapFunction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class mapFunction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def mapWord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mapFunction/mapWord',
            mainproto__pb2.MapText.SerializeToString,
            mainproto__pb2.MapNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class reduceFunctionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.redWord = channel.unary_unary(
                '/reduceFunction/redWord',
                request_serializer=mainproto__pb2.ReduceText.SerializeToString,
                response_deserializer=mainproto__pb2.ReduceNumber.FromString,
                )


class reduceFunctionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def redWord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_reduceFunctionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'redWord': grpc.unary_unary_rpc_method_handler(
                    servicer.redWord,
                    request_deserializer=mainproto__pb2.ReduceText.FromString,
                    response_serializer=mainproto__pb2.ReduceNumber.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reduceFunction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class reduceFunction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def redWord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reduceFunction/redWord',
            mainproto__pb2.ReduceText.SerializeToString,
            mainproto__pb2.ReduceNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)