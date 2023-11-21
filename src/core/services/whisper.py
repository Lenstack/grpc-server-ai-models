import torch
import whisper


def transcribe(model_name="base", device=("cuda" if torch.cuda.is_available() else "cpu"), fp16=False,
               initial_prompt="", audio="audio/records.wav"):
    # Load model from Whisper
    return "audio has been transcribed"
