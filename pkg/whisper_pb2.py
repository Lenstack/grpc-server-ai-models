# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: whisper.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rwhisper.proto\x12\x03pkg\"\x98\x01\n\x13SpeechToTextRequest\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\x12\n\naudio_file\x18\x02 \x01(\x0c\x12\x16\n\x0einitial_prompt\x18\x03 \x01(\t\x12\x17\n\x0flanguage_target\x18\x04 \x01(\t\x12\x15\n\routput_format\x18\x05 \x01(\t\x12\x17\n\x0fword_timestamps\x18\x06 \x01(\x08\"$\n\x14SpeechToTextResponse\x12\x0c\n\x04text\x18\x01 \x01(\t2U\n\x0cWhisperModel\x12\x45\n\x0cSpeechToText\x12\x18.pkg.SpeechToTextRequest\x1a\x19.pkg.SpeechToTextResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'whisper_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SPEECHTOTEXTREQUEST']._serialized_start=23
  _globals['_SPEECHTOTEXTREQUEST']._serialized_end=175
  _globals['_SPEECHTOTEXTRESPONSE']._serialized_start=177
  _globals['_SPEECHTOTEXTRESPONSE']._serialized_end=213
  _globals['_WHISPERMODEL']._serialized_start=215
  _globals['_WHISPERMODEL']._serialized_end=300
# @@protoc_insertion_point(module_scope)
