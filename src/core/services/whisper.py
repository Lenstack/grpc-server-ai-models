from datetime import datetime

from faster_whisper import WhisperModel


def transcribe(model_name="base", initial_prompt="", audio_file="", task="",
               language="", word_timestamps=False):
    if audio_file is None:
        return "No audio file found"

    audio_model = WhisperModel(model_name, device="cpu", compute_type="int8", download_root="../models",
                               local_files_only=True)
    segments, _ = audio_model.transcribe("../audio/records.wav", beam_size=5, task=task, language=language,
                                         word_timestamps=word_timestamps)
    response = ''.join(segment.text for segment in segments)

    # Store the response in a file with the current timestamp
    with open(f"../audio/records_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", "w") as f:
        f.write(response)

    return response
