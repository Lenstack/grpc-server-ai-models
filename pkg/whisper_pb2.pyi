from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SpeechToTextRequest(_message.Message):
    __slots__ = ["audio", "language_target", "output_format", "word_timestamps"]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TARGET_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    WORD_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    language_target: str
    output_format: str
    word_timestamps: bool
    def __init__(self, audio: _Optional[bytes] = ..., language_target: _Optional[str] = ..., output_format: _Optional[str] = ..., word_timestamps: bool = ...) -> None: ...

class SpeechToTextResponse(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
