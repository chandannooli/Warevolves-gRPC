# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: werewolves.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10werewolves.proto\x12\nwerewolves\"4\n\x0e\x43onnectRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x0f\x43onnectResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xf4\x01\n\x11WerewolvesService\x12\x44\n\x07\x43onnect\x12\x1a.werewolves.ConnectRequest\x1a\x1b.werewolves.ConnectResponse\"\x00\x12Q\n\x12InteractiveMessage\x12\x1a.werewolves.MessageRequest\x1a\x1b.werewolves.MessageResponse(\x01\x30\x01\x12\x46\n\tStartGame\x12\x1a.werewolves.MessageRequest\x1a\x1b.werewolves.MessageResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'werewolves_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CONNECTREQUEST']._serialized_start=32
  _globals['_CONNECTREQUEST']._serialized_end=84
  _globals['_CONNECTRESPONSE']._serialized_start=86
  _globals['_CONNECTRESPONSE']._serialized_end=120
  _globals['_MESSAGEREQUEST']._serialized_start=122
  _globals['_MESSAGEREQUEST']._serialized_end=155
  _globals['_MESSAGERESPONSE']._serialized_start=157
  _globals['_MESSAGERESPONSE']._serialized_end=191
  _globals['_WEREWOLVESSERVICE']._serialized_start=194
  _globals['_WEREWOLVESSERVICE']._serialized_end=438
# @@protoc_insertion_point(module_scope)