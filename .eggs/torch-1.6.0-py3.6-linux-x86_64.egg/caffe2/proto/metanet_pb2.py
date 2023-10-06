# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caffe2/proto/metanet.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from caffe2.proto import caffe2_pb2 as caffe2_dot_proto_dot_caffe2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='caffe2/proto/metanet.proto',
  package='caffe2',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x1a\x63\x61\x66\x66\x65\x32/proto/metanet.proto\x12\x06\x63\x61\x66\x66\x65\x32\x1a\x19\x63\x61\x66\x66\x65\x32/proto/caffe2.proto\"{\n\tModelInfo\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\nmodelClass\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\'\n\rpredictorType\x18\x04 \x01(\t:\x10SINGLE_PREDICTOR\x12\x0f\n\x07modelId\x18\x05 \x01(\t\"&\n\x08\x42lobsMap\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x03(\t\"5\n\x07NetsMap\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x1d\n\x05value\x18\x02 \x02(\x0b\x32\x0e.caffe2.NetDef\"7\n\x08PlansMap\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x1e\n\x05value\x18\x02 \x02(\x0b\x32\x0f.caffe2.PlanDef\"\'\n\tStringMap\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xa7\x02\n\nMetaNetDef\x12\x1f\n\x05\x62lobs\x18\x01 \x03(\x0b\x32\x10.caffe2.BlobsMap\x12\x1d\n\x04nets\x18\x02 \x03(\x0b\x32\x0f.caffe2.NetsMap\x12$\n\tmodelInfo\x18\x03 \x01(\x0b\x32\x11.caffe2.ModelInfo\x12\x1f\n\x05plans\x18\x04 \x03(\x0b\x32\x10.caffe2.PlansMap\x12\x32\n\x17\x61pplicationSpecificInfo\x18\x05 \x03(\x0b\x32\x11.caffe2.StringMap\x12\x12\n\nblobsOrder\x18\x06 \x03(\t\x12\x14\n\x0cpreLoadBlobs\x18\x07 \x03(\t\x12\x34\n\x11tensorBoundShapes\x18\x08 \x01(\x0b\x32\x19.caffe2.TensorBoundShapes'
  ,
  dependencies=[caffe2_dot_proto_dot_caffe2__pb2.DESCRIPTOR,])




_MODELINFO = _descriptor.Descriptor(
  name='ModelInfo',
  full_name='caffe2.ModelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='caffe2.ModelInfo.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelClass', full_name='caffe2.ModelInfo.modelClass', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='caffe2.ModelInfo.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predictorType', full_name='caffe2.ModelInfo.predictorType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"SINGLE_PREDICTOR".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelId', full_name='caffe2.ModelInfo.modelId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=188,
)


_BLOBSMAP = _descriptor.Descriptor(
  name='BlobsMap',
  full_name='caffe2.BlobsMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='caffe2.BlobsMap.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='caffe2.BlobsMap.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=228,
)


_NETSMAP = _descriptor.Descriptor(
  name='NetsMap',
  full_name='caffe2.NetsMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='caffe2.NetsMap.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='caffe2.NetsMap.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=230,
  serialized_end=283,
)


_PLANSMAP = _descriptor.Descriptor(
  name='PlansMap',
  full_name='caffe2.PlansMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='caffe2.PlansMap.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='caffe2.PlansMap.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=340,
)


_STRINGMAP = _descriptor.Descriptor(
  name='StringMap',
  full_name='caffe2.StringMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='caffe2.StringMap.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='caffe2.StringMap.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=381,
)


_METANETDEF = _descriptor.Descriptor(
  name='MetaNetDef',
  full_name='caffe2.MetaNetDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blobs', full_name='caffe2.MetaNetDef.blobs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nets', full_name='caffe2.MetaNetDef.nets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modelInfo', full_name='caffe2.MetaNetDef.modelInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plans', full_name='caffe2.MetaNetDef.plans', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applicationSpecificInfo', full_name='caffe2.MetaNetDef.applicationSpecificInfo', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobsOrder', full_name='caffe2.MetaNetDef.blobsOrder', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preLoadBlobs', full_name='caffe2.MetaNetDef.preLoadBlobs', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensorBoundShapes', full_name='caffe2.MetaNetDef.tensorBoundShapes', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=384,
  serialized_end=679,
)

_NETSMAP.fields_by_name['value'].message_type = caffe2_dot_proto_dot_caffe2__pb2._NETDEF
_PLANSMAP.fields_by_name['value'].message_type = caffe2_dot_proto_dot_caffe2__pb2._PLANDEF
_METANETDEF.fields_by_name['blobs'].message_type = _BLOBSMAP
_METANETDEF.fields_by_name['nets'].message_type = _NETSMAP
_METANETDEF.fields_by_name['modelInfo'].message_type = _MODELINFO
_METANETDEF.fields_by_name['plans'].message_type = _PLANSMAP
_METANETDEF.fields_by_name['applicationSpecificInfo'].message_type = _STRINGMAP
_METANETDEF.fields_by_name['tensorBoundShapes'].message_type = caffe2_dot_proto_dot_caffe2__pb2._TENSORBOUNDSHAPES
DESCRIPTOR.message_types_by_name['ModelInfo'] = _MODELINFO
DESCRIPTOR.message_types_by_name['BlobsMap'] = _BLOBSMAP
DESCRIPTOR.message_types_by_name['NetsMap'] = _NETSMAP
DESCRIPTOR.message_types_by_name['PlansMap'] = _PLANSMAP
DESCRIPTOR.message_types_by_name['StringMap'] = _STRINGMAP
DESCRIPTOR.message_types_by_name['MetaNetDef'] = _METANETDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelInfo = _reflection.GeneratedProtocolMessageType('ModelInfo', (_message.Message,), {
  'DESCRIPTOR' : _MODELINFO,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.ModelInfo)
  })
_sym_db.RegisterMessage(ModelInfo)

BlobsMap = _reflection.GeneratedProtocolMessageType('BlobsMap', (_message.Message,), {
  'DESCRIPTOR' : _BLOBSMAP,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.BlobsMap)
  })
_sym_db.RegisterMessage(BlobsMap)

NetsMap = _reflection.GeneratedProtocolMessageType('NetsMap', (_message.Message,), {
  'DESCRIPTOR' : _NETSMAP,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.NetsMap)
  })
_sym_db.RegisterMessage(NetsMap)

PlansMap = _reflection.GeneratedProtocolMessageType('PlansMap', (_message.Message,), {
  'DESCRIPTOR' : _PLANSMAP,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.PlansMap)
  })
_sym_db.RegisterMessage(PlansMap)

StringMap = _reflection.GeneratedProtocolMessageType('StringMap', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMAP,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.StringMap)
  })
_sym_db.RegisterMessage(StringMap)

MetaNetDef = _reflection.GeneratedProtocolMessageType('MetaNetDef', (_message.Message,), {
  'DESCRIPTOR' : _METANETDEF,
  '__module__' : 'caffe2.proto.metanet_pb2'
  # @@protoc_insertion_point(class_scope:caffe2.MetaNetDef)
  })
_sym_db.RegisterMessage(MetaNetDef)


# @@protoc_insertion_point(module_scope)
