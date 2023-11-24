from datetime import datetime
from faster_whisper import WhisperModel
from src.core.utils.output_format import isOutputFormat


def transcribe(model_name="base", initial_prompt="", audio_file="",
               task="", language="", output_format="", word_timestamps=False):
    if not audio_file:
        return "No audio file found or provided"

    try:
        audio_model = WhisperModel(model_name, device="cpu", compute_type="int8", download_root="../models",
                                   local_files_only=True)

        segments, info = audio_model.transcribe("../audio/records.wav", beam_size=5, task=task, language=language,
                                                word_timestamps=word_timestamps)

        response = isOutputFormat(segments, info, output_format)

        output_file = f"../audio/records_{datetime.now().strftime('%Y%m%d%H%M%S')}.{output_format}"
        with open(output_file, "w") as f:
            f.write(response)

        return response

    except Exception as e:
        return f"Transcription failed: {str(e)}"
