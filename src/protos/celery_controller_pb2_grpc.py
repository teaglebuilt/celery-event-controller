# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import celery_controller_pb2 as protos_dot_celery__controller__pb2


class EventServerStub(object):
    """
    Server objects.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.capture_realtime = channel.unary_stream(
                '/EventServer/capture_realtime',
                request_serializer=protos_dot_celery__controller__pb2.CaptureRequest.SerializeToString,
                response_deserializer=protos_dot_celery__controller__pb2.RealtimeMessage.FromString,
                )
        self.get_metrics = channel.unary_unary(
                '/EventServer/get_metrics',
                request_serializer=protos_dot_celery__controller__pb2.Null.SerializeToString,
                response_deserializer=protos_dot_celery__controller__pb2.StatsMessage.FromString,
                )


class EventServerServicer(object):
    """
    Server objects.

    """

    def capture_realtime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_metrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'capture_realtime': grpc.unary_stream_rpc_method_handler(
                    servicer.capture_realtime,
                    request_deserializer=protos_dot_celery__controller__pb2.CaptureRequest.FromString,
                    response_serializer=protos_dot_celery__controller__pb2.RealtimeMessage.SerializeToString,
            ),
            'get_metrics': grpc.unary_unary_rpc_method_handler(
                    servicer.get_metrics,
                    request_deserializer=protos_dot_celery__controller__pb2.Null.FromString,
                    response_serializer=protos_dot_celery__controller__pb2.StatsMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EventServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventServer(object):
    """
    Server objects.

    """

    @staticmethod
    def capture_realtime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/EventServer/capture_realtime',
            protos_dot_celery__controller__pb2.CaptureRequest.SerializeToString,
            protos_dot_celery__controller__pb2.RealtimeMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_metrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EventServer/get_metrics',
            protos_dot_celery__controller__pb2.Null.SerializeToString,
            protos_dot_celery__controller__pb2.StatsMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
