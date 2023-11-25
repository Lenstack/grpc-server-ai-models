from faster_whisper import WhisperModel
from src.core.utils.output_format import isOutputFormat

# Create the model instance outside the function to reuse it if possible
audio_model = WhisperModel("base", device="cpu", compute_type="int8", download_root="../models")


def transcribe(initial_prompt="", audio_file="", task="", language="", output_format="", word_timestamps=False):
    if not audio_file:
        return "No audio file found or provided"

    try:
        global audio_model  # Use the model instance defined outside the function

        segments, info = audio_model.transcribe("../audio/records.wav", beam_size=5, task=task, language=language,
                                                initial_prompt=initial_prompt, word_timestamps=word_timestamps)

        response = isOutputFormat(segments, info, output_format)

        output_file = f"../audio/records_output.{output_format}"
        with open(output_file, "w") as f:
            f.write(response)

        return response

    except Exception as e:
        return f"Transcription failed: {str(e)}"
