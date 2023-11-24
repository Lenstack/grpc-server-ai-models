from datetime import datetime
from faster_whisper import WhisperModel


def transcribe(model_name="base", initial_prompt="", audio_file="",
               task="", language="", output_format="", word_timestamps=False):
    if not audio_file:
        return "No audio file found or provided"

    try:
        audio_model = WhisperModel(model_name, device="cpu", compute_type="int8", download_root="../models",
                                   local_files_only=True)
        segments, _ = audio_model.transcribe("../audio/records.wav", beam_size=5, task=task, language=language,
                                             word_timestamps=word_timestamps)
        response = ''.join(segment.text for segment in segments)

        # Store the response in a file with the current timestamp
        output_file = f"../audio/records_{datetime.now().strftime('%Y%m%d%H%M%S')}.{output_format}"
        with open(output_file, "w") as f:
            f.write(response)

            if output_format == "json":
                from src.core.utils.output_format import to_json
                response = to_json(response)
            elif output_format == "txt":
                response = response

        return response

    except Exception as e:
        return f"Transcription failed: {str(e)}"
