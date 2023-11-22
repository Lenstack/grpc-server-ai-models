from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TextToSpeechRequest(_message.Message):
    __slots__ = ["text", "speaker_voice", "language"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_VOICE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    text: str
    speaker_voice: str
    language: str
    def __init__(self, text: _Optional[str] = ..., speaker_voice: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class TextToSpeechResponse(_message.Message):
    __slots__ = ["audio"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    def __init__(self, audio: _Optional[bytes] = ...) -> None: ...
