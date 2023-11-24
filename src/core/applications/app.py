from pkg import whisper_pb2_grpc, piper_pb2_grpc, whisper_pb2, piper_pb2
from src.core.services.piper import speech
from src.core.services.whisper import transcribe


class WhisperImplementation(whisper_pb2_grpc.WhisperModelServicer):
    def SpeechToText(self, request, context):
        response = whisper_pb2.SpeechToTextResponse()
        try:
            print("Received audio data...")
            # Transcribe each audio request
            transcription = transcribe(audio_file=request.audio_file, language=request.language_target,
                                       task=request.task, initial_prompt=request.initial_prompt,
                                       output_format=request.output_format, word_timestamps=request.word_timestamps)
            # Assuming response has a field called 'transcription' to store the result
            response.text = transcription
            print(f"Transcription: {transcription}")
        except Exception as e:
            print(f"Error occurred during transcription: {e}")
        return response


class PiperServiceImplementation(piper_pb2_grpc.PiperModelServicer):
    def TextToSpeech(self, request, context):
        response = piper_pb2.TextToSpeechResponse()
        # Assuming request_iterator contains text data in each request
        try:
            print("Received text data...")
            # Synthesize each text request
            audio = speech(text=request.text, speaker_voice=request.speaker_voice, language=request.language_target)
            # Assuming response has a field called 'audio' to store the result
            response.audio = audio
            print(f"Audio: {audio}")
        except Exception as e:
            print(f"Error occurred during synthesis: {e}")
        return response
