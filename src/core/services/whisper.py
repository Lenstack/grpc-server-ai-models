import whisper


def transcribe(model_name="base", initial_prompt="", audio_file="audio/records.wav", task="translate",
               language="en"):
    audio_model = whisper.load_model(model_name)
    response = audio_model.transcribe(audio_file, initial_prompt, task, language)
    return response["text"]
