# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import werewolves_pb2 as werewolves__pb2


class ChatServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChatStream = channel.unary_stream(
                '/grpc.ChatServer/ChatStream',
                request_serializer=werewolves__pb2.Name.SerializeToString,
                response_deserializer=werewolves__pb2.Message.FromString,
                )
        self.HandleMessage = channel.unary_unary(
                '/grpc.ChatServer/HandleMessage',
                request_serializer=werewolves__pb2.Message.SerializeToString,
                response_deserializer=werewolves__pb2.Empty.FromString,
                )
        self.Connect = channel.unary_unary(
                '/grpc.ChatServer/Connect',
                request_serializer=werewolves__pb2.Credentials.SerializeToString,
                response_deserializer=werewolves__pb2.Message.FromString,
                )


class ChatServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChatStream(self, request, context):
        """This bi-directional stream makes it possible to send and receive Notes between 2 persons
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChatStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ChatStream,
                    request_deserializer=werewolves__pb2.Name.FromString,
                    response_serializer=werewolves__pb2.Message.SerializeToString,
            ),
            'HandleMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleMessage,
                    request_deserializer=werewolves__pb2.Message.FromString,
                    response_serializer=werewolves__pb2.Empty.SerializeToString,
            ),
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=werewolves__pb2.Credentials.FromString,
                    response_serializer=werewolves__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ChatServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChatStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.ChatServer/ChatStream',
            werewolves__pb2.Name.SerializeToString,
            werewolves__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HandleMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/HandleMessage',
            werewolves__pb2.Message.SerializeToString,
            werewolves__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatServer/Connect',
            werewolves__pb2.Credentials.SerializeToString,
            werewolves__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
