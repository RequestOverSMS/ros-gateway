# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ROSRequest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ROSEnums_pb2 as ROSEnums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10ROSRequest.proto\x1a\x0eROSEnums.proto\"o\n\nROSRequest\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x05.Type:\x07REQUEST\x12\x17\n\x06method\x18\x02 \x01(\x0e\x32\x07.Method\x12\x0b\n\x03uri\x18\x04 \x01(\t\x12\x0f\n\x07headers\x18\x05 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x06 \x01(\x0c')



_ROSREQUEST = DESCRIPTOR.message_types_by_name['ROSRequest']
ROSRequest = _reflection.GeneratedProtocolMessageType('ROSRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROSREQUEST,
  '__module__' : 'ROSRequest_pb2'
  # @@protoc_insertion_point(class_scope:ROSRequest)
  })
_sym_db.RegisterMessage(ROSRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROSREQUEST._serialized_start=36
  _ROSREQUEST._serialized_end=147
# @@protoc_insertion_point(module_scope)