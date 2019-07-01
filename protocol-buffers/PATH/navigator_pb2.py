# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PATH/navigator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from PATH import collector_pb2 as PATH_dot_collector__pb2
from PATH import web_pb2 as PATH_dot_web__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PATH/navigator.proto',
  package='taurus',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14PATH/navigator.proto\x12\x06taurus\x1a\x14PATH/collector.proto\x1a\x0ePATH/web.proto\"#\n\x10\x43\x61ndlestickReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\tPortfolio\x12\x1d\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\r.taurus.Asset\"\'\n\x05\x41sset\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x32\x8f\x01\n\tNavigator\x12\x45\n\x0fPutCandlesticks\x12\x16.taurus.CandlestickSet\x1a\x18.taurus.CandlestickReply\"\x00\x12;\n\x0fInformPortfolio\x12\x11.taurus.Portfolio\x1a\x13.taurus.InformReply\"\x00\x62\x06proto3')
  ,
  dependencies=[PATH_dot_collector__pb2.DESCRIPTOR,PATH_dot_web__pb2.DESCRIPTOR,])




_CANDLESTICKREPLY = _descriptor.Descriptor(
  name='CandlestickReply',
  full_name='taurus.CandlestickReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='taurus.CandlestickReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=105,
)


_PORTFOLIO = _descriptor.Descriptor(
  name='Portfolio',
  full_name='taurus.Portfolio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='taurus.Portfolio.assets', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=149,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='taurus.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Symbol', full_name='taurus.Asset.Symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='taurus.Asset.amount', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=190,
)

_PORTFOLIO.fields_by_name['assets'].message_type = _ASSET
DESCRIPTOR.message_types_by_name['CandlestickReply'] = _CANDLESTICKREPLY
DESCRIPTOR.message_types_by_name['Portfolio'] = _PORTFOLIO
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CandlestickReply = _reflection.GeneratedProtocolMessageType('CandlestickReply', (_message.Message,), {
  'DESCRIPTOR' : _CANDLESTICKREPLY,
  '__module__' : 'PATH.navigator_pb2'
  # @@protoc_insertion_point(class_scope:taurus.CandlestickReply)
  })
_sym_db.RegisterMessage(CandlestickReply)

Portfolio = _reflection.GeneratedProtocolMessageType('Portfolio', (_message.Message,), {
  'DESCRIPTOR' : _PORTFOLIO,
  '__module__' : 'PATH.navigator_pb2'
  # @@protoc_insertion_point(class_scope:taurus.Portfolio)
  })
_sym_db.RegisterMessage(Portfolio)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'PATH.navigator_pb2'
  # @@protoc_insertion_point(class_scope:taurus.Asset)
  })
_sym_db.RegisterMessage(Asset)



_NAVIGATOR = _descriptor.ServiceDescriptor(
  name='Navigator',
  full_name='taurus.Navigator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=193,
  serialized_end=336,
  methods=[
  _descriptor.MethodDescriptor(
    name='PutCandlesticks',
    full_name='taurus.Navigator.PutCandlesticks',
    index=0,
    containing_service=None,
    input_type=PATH_dot_collector__pb2._CANDLESTICKSET,
    output_type=_CANDLESTICKREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InformPortfolio',
    full_name='taurus.Navigator.InformPortfolio',
    index=1,
    containing_service=None,
    input_type=_PORTFOLIO,
    output_type=PATH_dot_web__pb2._INFORMREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAVIGATOR)

DESCRIPTOR.services_by_name['Navigator'] = _NAVIGATOR

# @@protoc_insertion_point(module_scope)
