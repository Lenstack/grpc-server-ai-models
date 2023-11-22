import whisper


def transcribe(model_name="base", initial_prompt="", audio_file="audio/records.wav", task="translate",
               language="en", word_timestamps=False):
    audio_model = whisper.load_model(model_name, download_root="../models")
    audio = whisper.load_audio(audio_file)

    response = audio_model.transcribe(audio=audio, fp16=False, task=task, language=language,
                                      initial_prompt=initial_prompt, word_timestamps=word_timestamps)
    return response["text"]
