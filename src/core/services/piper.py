import torch


def speech(model_name="",
           device=("cuda" if torch.cuda.is_available() else "cpu"), text="",
           speaker_wav="my/cloning/audio.wav", language="en"
           ):
    # Load the model from the Piper
    return
