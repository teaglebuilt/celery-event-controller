import grpc
import logging
from concurrent import futures
from queue import Empty, Queue
from typing import Optional
from contextlib import ExitStack
from protos.celery_controller_pb2 import EventServerServicer, add_EventServerServicer_to_server
from protos.celery_controller_pb2 import (
    TaskMessage,
    WorkerMessage,
    RealtimeMessage,
    StatsMessage,
    Null
)

logger = logging.getLogger(__name__)


class RPCService(EventServerServicer):

    def capture_realtime(self, request, context):
        queue = Queue()
        print('We got something')



def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_EventServerServicer_to_server(RPCService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()