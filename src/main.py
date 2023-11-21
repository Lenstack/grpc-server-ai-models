from src.core.adapters.grpc.server import GRPCServer

if __name__ == '__main__':
    try:
        grpc_server = GRPCServer()
    except Exception as e:
        print(f"Error occurred during server instantiation: {e}")
