from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection

from pkg import whisper_pb2_grpc, piper_pb2_grpc, whisper_pb2, piper_pb2
from src.core.applications.app import WhisperImplementation, PiperServiceImplementation


def GRPCServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    whisper_pb2_grpc.add_WhisperModelServicer_to_server(WhisperImplementation(), server)
    piper_pb2_grpc.add_PiperModelServicer_to_server(PiperServiceImplementation(), server)

    SERVICE_NAMES = (
        whisper_pb2.DESCRIPTOR.services_by_name['WhisperModel'].full_name,
        piper_pb2.DESCRIPTOR.services_by_name['PiperModel'].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()
