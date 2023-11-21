from pkg import whisper_pb2_grpc, piper_pb2_grpc, whisper_pb2, piper_pb2
from src.core.services.piper import speech
from src.core.services.whisper import transcribe


class WhisperImplementation(whisper_pb2_grpc.WhisperModelServicer):
    def SpeechToText(self, request_iterator, context):
        response = whisper_pb2.SpeechToTextResponse()
        # Assuming request_iterator contains audio data in each request
        for request in request_iterator:
            try:
                print("Received audio data..." + str(len(request.audio)))
                # Transcribe each audio request
                transcription = transcribe(audio=request.audio)
                # Assuming response has a field called 'transcription' to store the result
                response.text = transcription
            except Exception as e:
                print(f"Error occurred during transcription: {e}")
        return response


class PiperServiceImplementation(piper_pb2_grpc.PiperModelServicer):
    def TextToSpeech(self, request_iterator, context):
        response = piper_pb2.TextToSpeechResponse()
        # Assuming request_iterator contains text data in each request
        for request in request_iterator:
            try:
                print("Received text data..." + request.text)
                # Synthesize each text request
                audio = speech(text=request.text)
                # Assuming response has a field called 'audio' to store the result
                response.audio = audio
            except Exception as e:
                print(f"Error occurred during synthesis: {e}")
        return response
