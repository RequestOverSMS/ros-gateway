# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1_market_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18v1_market_response.proto\x1a\x19google/protobuf/any.proto\"\xea\x41\n\tv1_market\x12!\n\x06object\x18\x01 \x01(\x0b\x32\x11.v1_market.Object\x12$\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x1a\xa4\x01\n\x06\x44\x61iars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x42tcars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x42tcdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xba\x01\n\x06\x42tcust\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xba\x01\n\x06\x44\x61iusd\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x45thars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x45thdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xba\x01\n\x06\x45thust\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x41\x64\x61\x61rs\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x41\x64\x61\x64\x61i\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x42nbdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x42nbars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa6\x01\n\x08Maticars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa6\x01\n\x08Maticdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x44otars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06\x44otdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06Solars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06Soldai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07Usdtars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07Usdtdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbd\x01\n\tUsdtnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07Usdcars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07Usdcdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbd\x01\n\tUsdcnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07\x42usdars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa5\x01\n\x07\x42usddai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbd\x01\n\tBusdnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06Ustars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa4\x01\n\x06Ustdai\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08Ustnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xa6\x01\n\x08Nuarsars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12\x12\n\nopen_price\x18\x06 \x01(\t\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x41\x64\x61nuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x42nbnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x42tcnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x44\x61inuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x44otnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08\x45thnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbe\x01\n\nMaticnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xbc\x01\n\x08Solnuars\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x14\n\x0c\x62id_currency\x18\x02 \x01(\t\x12\x14\n\x0c\x61sk_currency\x18\x03 \x01(\t\x12\x16\n\x0epurchase_price\x18\x04 \x01(\t\x12\x15\n\rselling_price\x18\x05 \x01(\t\x12(\n\nopen_price\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11market_identifier\x18\x07 \x01(\t\x1a\xaf\x0b\n\x06Object\x12!\n\x06\x64\x61iars\x18\x01 \x01(\x0b\x32\x11.v1_market.Daiars\x12!\n\x06\x62tcars\x18\x02 \x01(\x0b\x32\x11.v1_market.Btcars\x12!\n\x06\x62tcdai\x18\x03 \x01(\x0b\x32\x11.v1_market.Btcdai\x12!\n\x06\x62tcust\x18\x04 \x01(\x0b\x32\x11.v1_market.Btcust\x12!\n\x06\x64\x61iusd\x18\x05 \x01(\x0b\x32\x11.v1_market.Daiusd\x12!\n\x06\x65thars\x18\x06 \x01(\x0b\x32\x11.v1_market.Ethars\x12!\n\x06\x65thdai\x18\x07 \x01(\x0b\x32\x11.v1_market.Ethdai\x12!\n\x06\x65thust\x18\x08 \x01(\x0b\x32\x11.v1_market.Ethust\x12!\n\x06\x61\x64\x61\x61rs\x18\t \x01(\x0b\x32\x11.v1_market.Adaars\x12!\n\x06\x61\x64\x61\x64\x61i\x18\n \x01(\x0b\x32\x11.v1_market.Adadai\x12!\n\x06\x62nbdai\x18\x0b \x01(\x0b\x32\x11.v1_market.Bnbdai\x12!\n\x06\x62nbars\x18\x0c \x01(\x0b\x32\x11.v1_market.Bnbars\x12%\n\x08maticars\x18\r \x01(\x0b\x32\x13.v1_market.Maticars\x12%\n\x08maticdai\x18\x0e \x01(\x0b\x32\x13.v1_market.Maticdai\x12!\n\x06\x64otars\x18\x0f \x01(\x0b\x32\x11.v1_market.Dotars\x12!\n\x06\x64otdai\x18\x10 \x01(\x0b\x32\x11.v1_market.Dotdai\x12!\n\x06solars\x18\x11 \x01(\x0b\x32\x11.v1_market.Solars\x12!\n\x06soldai\x18\x12 \x01(\x0b\x32\x11.v1_market.Soldai\x12#\n\x07usdtars\x18\x13 \x01(\x0b\x32\x12.v1_market.Usdtars\x12#\n\x07usdtdai\x18\x14 \x01(\x0b\x32\x12.v1_market.Usdtdai\x12\'\n\tusdtnuars\x18\x15 \x01(\x0b\x32\x14.v1_market.Usdtnuars\x12#\n\x07usdcars\x18\x16 \x01(\x0b\x32\x12.v1_market.Usdcars\x12#\n\x07usdcdai\x18\x17 \x01(\x0b\x32\x12.v1_market.Usdcdai\x12\'\n\tusdcnuars\x18\x18 \x01(\x0b\x32\x14.v1_market.Usdcnuars\x12#\n\x07\x62usdars\x18\x19 \x01(\x0b\x32\x12.v1_market.Busdars\x12#\n\x07\x62usddai\x18\x1a \x01(\x0b\x32\x12.v1_market.Busddai\x12\'\n\tbusdnuars\x18\x1b \x01(\x0b\x32\x14.v1_market.Busdnuars\x12!\n\x06ustars\x18\x1c \x01(\x0b\x32\x11.v1_market.Ustars\x12!\n\x06ustdai\x18\x1d \x01(\x0b\x32\x11.v1_market.Ustdai\x12%\n\x08ustnuars\x18\x1e \x01(\x0b\x32\x13.v1_market.Ustnuars\x12%\n\x08nuarsars\x18\x1f \x01(\x0b\x32\x13.v1_market.Nuarsars\x12%\n\x08\x61\x64\x61nuars\x18  \x01(\x0b\x32\x13.v1_market.Adanuars\x12%\n\x08\x62nbnuars\x18! \x01(\x0b\x32\x13.v1_market.Bnbnuars\x12%\n\x08\x62tcnuars\x18\" \x01(\x0b\x32\x13.v1_market.Btcnuars\x12%\n\x08\x64\x61inuars\x18# \x01(\x0b\x32\x13.v1_market.Dainuars\x12%\n\x08\x64otnuars\x18$ \x01(\x0b\x32\x13.v1_market.Dotnuars\x12%\n\x08\x65thnuars\x18% \x01(\x0b\x32\x13.v1_market.Ethnuars\x12)\n\nmaticnuars\x18& \x01(\x0b\x32\x15.v1_market.Maticnuars\x12%\n\x08solnuars\x18\' \x01(\x0b\x32\x13.v1_market.Solnuarsb\x06proto3')



_V1_MARKET = DESCRIPTOR.message_types_by_name['v1_market']
_V1_MARKET_DAIARS = _V1_MARKET.nested_types_by_name['Daiars']
_V1_MARKET_BTCARS = _V1_MARKET.nested_types_by_name['Btcars']
_V1_MARKET_BTCDAI = _V1_MARKET.nested_types_by_name['Btcdai']
_V1_MARKET_BTCUST = _V1_MARKET.nested_types_by_name['Btcust']
_V1_MARKET_DAIUSD = _V1_MARKET.nested_types_by_name['Daiusd']
_V1_MARKET_ETHARS = _V1_MARKET.nested_types_by_name['Ethars']
_V1_MARKET_ETHDAI = _V1_MARKET.nested_types_by_name['Ethdai']
_V1_MARKET_ETHUST = _V1_MARKET.nested_types_by_name['Ethust']
_V1_MARKET_ADAARS = _V1_MARKET.nested_types_by_name['Adaars']
_V1_MARKET_ADADAI = _V1_MARKET.nested_types_by_name['Adadai']
_V1_MARKET_BNBDAI = _V1_MARKET.nested_types_by_name['Bnbdai']
_V1_MARKET_BNBARS = _V1_MARKET.nested_types_by_name['Bnbars']
_V1_MARKET_MATICARS = _V1_MARKET.nested_types_by_name['Maticars']
_V1_MARKET_MATICDAI = _V1_MARKET.nested_types_by_name['Maticdai']
_V1_MARKET_DOTARS = _V1_MARKET.nested_types_by_name['Dotars']
_V1_MARKET_DOTDAI = _V1_MARKET.nested_types_by_name['Dotdai']
_V1_MARKET_SOLARS = _V1_MARKET.nested_types_by_name['Solars']
_V1_MARKET_SOLDAI = _V1_MARKET.nested_types_by_name['Soldai']
_V1_MARKET_USDTARS = _V1_MARKET.nested_types_by_name['Usdtars']
_V1_MARKET_USDTDAI = _V1_MARKET.nested_types_by_name['Usdtdai']
_V1_MARKET_USDTNUARS = _V1_MARKET.nested_types_by_name['Usdtnuars']
_V1_MARKET_USDCARS = _V1_MARKET.nested_types_by_name['Usdcars']
_V1_MARKET_USDCDAI = _V1_MARKET.nested_types_by_name['Usdcdai']
_V1_MARKET_USDCNUARS = _V1_MARKET.nested_types_by_name['Usdcnuars']
_V1_MARKET_BUSDARS = _V1_MARKET.nested_types_by_name['Busdars']
_V1_MARKET_BUSDDAI = _V1_MARKET.nested_types_by_name['Busddai']
_V1_MARKET_BUSDNUARS = _V1_MARKET.nested_types_by_name['Busdnuars']
_V1_MARKET_USTARS = _V1_MARKET.nested_types_by_name['Ustars']
_V1_MARKET_USTDAI = _V1_MARKET.nested_types_by_name['Ustdai']
_V1_MARKET_USTNUARS = _V1_MARKET.nested_types_by_name['Ustnuars']
_V1_MARKET_NUARSARS = _V1_MARKET.nested_types_by_name['Nuarsars']
_V1_MARKET_ADANUARS = _V1_MARKET.nested_types_by_name['Adanuars']
_V1_MARKET_BNBNUARS = _V1_MARKET.nested_types_by_name['Bnbnuars']
_V1_MARKET_BTCNUARS = _V1_MARKET.nested_types_by_name['Btcnuars']
_V1_MARKET_DAINUARS = _V1_MARKET.nested_types_by_name['Dainuars']
_V1_MARKET_DOTNUARS = _V1_MARKET.nested_types_by_name['Dotnuars']
_V1_MARKET_ETHNUARS = _V1_MARKET.nested_types_by_name['Ethnuars']
_V1_MARKET_MATICNUARS = _V1_MARKET.nested_types_by_name['Maticnuars']
_V1_MARKET_SOLNUARS = _V1_MARKET.nested_types_by_name['Solnuars']
_V1_MARKET_OBJECT = _V1_MARKET.nested_types_by_name['Object']
v1_market = _reflection.GeneratedProtocolMessageType('v1_market', (_message.Message,), {

  'Daiars' : _reflection.GeneratedProtocolMessageType('Daiars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DAIARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Daiars)
    })
  ,

  'Btcars' : _reflection.GeneratedProtocolMessageType('Btcars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BTCARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Btcars)
    })
  ,

  'Btcdai' : _reflection.GeneratedProtocolMessageType('Btcdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BTCDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Btcdai)
    })
  ,

  'Btcust' : _reflection.GeneratedProtocolMessageType('Btcust', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BTCUST,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Btcust)
    })
  ,

  'Daiusd' : _reflection.GeneratedProtocolMessageType('Daiusd', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DAIUSD,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Daiusd)
    })
  ,

  'Ethars' : _reflection.GeneratedProtocolMessageType('Ethars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ETHARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ethars)
    })
  ,

  'Ethdai' : _reflection.GeneratedProtocolMessageType('Ethdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ETHDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ethdai)
    })
  ,

  'Ethust' : _reflection.GeneratedProtocolMessageType('Ethust', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ETHUST,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ethust)
    })
  ,

  'Adaars' : _reflection.GeneratedProtocolMessageType('Adaars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ADAARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Adaars)
    })
  ,

  'Adadai' : _reflection.GeneratedProtocolMessageType('Adadai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ADADAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Adadai)
    })
  ,

  'Bnbdai' : _reflection.GeneratedProtocolMessageType('Bnbdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BNBDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Bnbdai)
    })
  ,

  'Bnbars' : _reflection.GeneratedProtocolMessageType('Bnbars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BNBARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Bnbars)
    })
  ,

  'Maticars' : _reflection.GeneratedProtocolMessageType('Maticars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_MATICARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Maticars)
    })
  ,

  'Maticdai' : _reflection.GeneratedProtocolMessageType('Maticdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_MATICDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Maticdai)
    })
  ,

  'Dotars' : _reflection.GeneratedProtocolMessageType('Dotars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DOTARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Dotars)
    })
  ,

  'Dotdai' : _reflection.GeneratedProtocolMessageType('Dotdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DOTDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Dotdai)
    })
  ,

  'Solars' : _reflection.GeneratedProtocolMessageType('Solars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_SOLARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Solars)
    })
  ,

  'Soldai' : _reflection.GeneratedProtocolMessageType('Soldai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_SOLDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Soldai)
    })
  ,

  'Usdtars' : _reflection.GeneratedProtocolMessageType('Usdtars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDTARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdtars)
    })
  ,

  'Usdtdai' : _reflection.GeneratedProtocolMessageType('Usdtdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDTDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdtdai)
    })
  ,

  'Usdtnuars' : _reflection.GeneratedProtocolMessageType('Usdtnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDTNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdtnuars)
    })
  ,

  'Usdcars' : _reflection.GeneratedProtocolMessageType('Usdcars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDCARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdcars)
    })
  ,

  'Usdcdai' : _reflection.GeneratedProtocolMessageType('Usdcdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDCDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdcdai)
    })
  ,

  'Usdcnuars' : _reflection.GeneratedProtocolMessageType('Usdcnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USDCNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Usdcnuars)
    })
  ,

  'Busdars' : _reflection.GeneratedProtocolMessageType('Busdars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BUSDARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Busdars)
    })
  ,

  'Busddai' : _reflection.GeneratedProtocolMessageType('Busddai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BUSDDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Busddai)
    })
  ,

  'Busdnuars' : _reflection.GeneratedProtocolMessageType('Busdnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BUSDNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Busdnuars)
    })
  ,

  'Ustars' : _reflection.GeneratedProtocolMessageType('Ustars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USTARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ustars)
    })
  ,

  'Ustdai' : _reflection.GeneratedProtocolMessageType('Ustdai', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USTDAI,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ustdai)
    })
  ,

  'Ustnuars' : _reflection.GeneratedProtocolMessageType('Ustnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_USTNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ustnuars)
    })
  ,

  'Nuarsars' : _reflection.GeneratedProtocolMessageType('Nuarsars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_NUARSARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Nuarsars)
    })
  ,

  'Adanuars' : _reflection.GeneratedProtocolMessageType('Adanuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ADANUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Adanuars)
    })
  ,

  'Bnbnuars' : _reflection.GeneratedProtocolMessageType('Bnbnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BNBNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Bnbnuars)
    })
  ,

  'Btcnuars' : _reflection.GeneratedProtocolMessageType('Btcnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_BTCNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Btcnuars)
    })
  ,

  'Dainuars' : _reflection.GeneratedProtocolMessageType('Dainuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DAINUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Dainuars)
    })
  ,

  'Dotnuars' : _reflection.GeneratedProtocolMessageType('Dotnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_DOTNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Dotnuars)
    })
  ,

  'Ethnuars' : _reflection.GeneratedProtocolMessageType('Ethnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_ETHNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Ethnuars)
    })
  ,

  'Maticnuars' : _reflection.GeneratedProtocolMessageType('Maticnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_MATICNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Maticnuars)
    })
  ,

  'Solnuars' : _reflection.GeneratedProtocolMessageType('Solnuars', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_SOLNUARS,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Solnuars)
    })
  ,

  'Object' : _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
    'DESCRIPTOR' : _V1_MARKET_OBJECT,
    '__module__' : 'v1_market_response_pb2'
    # @@protoc_insertion_point(class_scope:v1_market.Object)
    })
  ,
  'DESCRIPTOR' : _V1_MARKET,
  '__module__' : 'v1_market_response_pb2'
  # @@protoc_insertion_point(class_scope:v1_market)
  })
_sym_db.RegisterMessage(v1_market)
_sym_db.RegisterMessage(v1_market.Daiars)
_sym_db.RegisterMessage(v1_market.Btcars)
_sym_db.RegisterMessage(v1_market.Btcdai)
_sym_db.RegisterMessage(v1_market.Btcust)
_sym_db.RegisterMessage(v1_market.Daiusd)
_sym_db.RegisterMessage(v1_market.Ethars)
_sym_db.RegisterMessage(v1_market.Ethdai)
_sym_db.RegisterMessage(v1_market.Ethust)
_sym_db.RegisterMessage(v1_market.Adaars)
_sym_db.RegisterMessage(v1_market.Adadai)
_sym_db.RegisterMessage(v1_market.Bnbdai)
_sym_db.RegisterMessage(v1_market.Bnbars)
_sym_db.RegisterMessage(v1_market.Maticars)
_sym_db.RegisterMessage(v1_market.Maticdai)
_sym_db.RegisterMessage(v1_market.Dotars)
_sym_db.RegisterMessage(v1_market.Dotdai)
_sym_db.RegisterMessage(v1_market.Solars)
_sym_db.RegisterMessage(v1_market.Soldai)
_sym_db.RegisterMessage(v1_market.Usdtars)
_sym_db.RegisterMessage(v1_market.Usdtdai)
_sym_db.RegisterMessage(v1_market.Usdtnuars)
_sym_db.RegisterMessage(v1_market.Usdcars)
_sym_db.RegisterMessage(v1_market.Usdcdai)
_sym_db.RegisterMessage(v1_market.Usdcnuars)
_sym_db.RegisterMessage(v1_market.Busdars)
_sym_db.RegisterMessage(v1_market.Busddai)
_sym_db.RegisterMessage(v1_market.Busdnuars)
_sym_db.RegisterMessage(v1_market.Ustars)
_sym_db.RegisterMessage(v1_market.Ustdai)
_sym_db.RegisterMessage(v1_market.Ustnuars)
_sym_db.RegisterMessage(v1_market.Nuarsars)
_sym_db.RegisterMessage(v1_market.Adanuars)
_sym_db.RegisterMessage(v1_market.Bnbnuars)
_sym_db.RegisterMessage(v1_market.Btcnuars)
_sym_db.RegisterMessage(v1_market.Dainuars)
_sym_db.RegisterMessage(v1_market.Dotnuars)
_sym_db.RegisterMessage(v1_market.Ethnuars)
_sym_db.RegisterMessage(v1_market.Maticnuars)
_sym_db.RegisterMessage(v1_market.Solnuars)
_sym_db.RegisterMessage(v1_market.Object)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _V1_MARKET._serialized_start=56
  _V1_MARKET._serialized_end=8482
  _V1_MARKET_DAIARS._serialized_start=143
  _V1_MARKET_DAIARS._serialized_end=307
  _V1_MARKET_BTCARS._serialized_start=310
  _V1_MARKET_BTCARS._serialized_end=474
  _V1_MARKET_BTCDAI._serialized_start=477
  _V1_MARKET_BTCDAI._serialized_end=641
  _V1_MARKET_BTCUST._serialized_start=644
  _V1_MARKET_BTCUST._serialized_end=830
  _V1_MARKET_DAIUSD._serialized_start=833
  _V1_MARKET_DAIUSD._serialized_end=1019
  _V1_MARKET_ETHARS._serialized_start=1022
  _V1_MARKET_ETHARS._serialized_end=1186
  _V1_MARKET_ETHDAI._serialized_start=1189
  _V1_MARKET_ETHDAI._serialized_end=1353
  _V1_MARKET_ETHUST._serialized_start=1356
  _V1_MARKET_ETHUST._serialized_end=1542
  _V1_MARKET_ADAARS._serialized_start=1545
  _V1_MARKET_ADAARS._serialized_end=1709
  _V1_MARKET_ADADAI._serialized_start=1712
  _V1_MARKET_ADADAI._serialized_end=1876
  _V1_MARKET_BNBDAI._serialized_start=1879
  _V1_MARKET_BNBDAI._serialized_end=2043
  _V1_MARKET_BNBARS._serialized_start=2046
  _V1_MARKET_BNBARS._serialized_end=2210
  _V1_MARKET_MATICARS._serialized_start=2213
  _V1_MARKET_MATICARS._serialized_end=2379
  _V1_MARKET_MATICDAI._serialized_start=2382
  _V1_MARKET_MATICDAI._serialized_end=2548
  _V1_MARKET_DOTARS._serialized_start=2551
  _V1_MARKET_DOTARS._serialized_end=2715
  _V1_MARKET_DOTDAI._serialized_start=2718
  _V1_MARKET_DOTDAI._serialized_end=2882
  _V1_MARKET_SOLARS._serialized_start=2885
  _V1_MARKET_SOLARS._serialized_end=3049
  _V1_MARKET_SOLDAI._serialized_start=3052
  _V1_MARKET_SOLDAI._serialized_end=3216
  _V1_MARKET_USDTARS._serialized_start=3219
  _V1_MARKET_USDTARS._serialized_end=3384
  _V1_MARKET_USDTDAI._serialized_start=3387
  _V1_MARKET_USDTDAI._serialized_end=3552
  _V1_MARKET_USDTNUARS._serialized_start=3555
  _V1_MARKET_USDTNUARS._serialized_end=3744
  _V1_MARKET_USDCARS._serialized_start=3747
  _V1_MARKET_USDCARS._serialized_end=3912
  _V1_MARKET_USDCDAI._serialized_start=3915
  _V1_MARKET_USDCDAI._serialized_end=4080
  _V1_MARKET_USDCNUARS._serialized_start=4083
  _V1_MARKET_USDCNUARS._serialized_end=4272
  _V1_MARKET_BUSDARS._serialized_start=4275
  _V1_MARKET_BUSDARS._serialized_end=4440
  _V1_MARKET_BUSDDAI._serialized_start=4443
  _V1_MARKET_BUSDDAI._serialized_end=4608
  _V1_MARKET_BUSDNUARS._serialized_start=4611
  _V1_MARKET_BUSDNUARS._serialized_end=4800
  _V1_MARKET_USTARS._serialized_start=4803
  _V1_MARKET_USTARS._serialized_end=4967
  _V1_MARKET_USTDAI._serialized_start=4970
  _V1_MARKET_USTDAI._serialized_end=5134
  _V1_MARKET_USTNUARS._serialized_start=5137
  _V1_MARKET_USTNUARS._serialized_end=5325
  _V1_MARKET_NUARSARS._serialized_start=5328
  _V1_MARKET_NUARSARS._serialized_end=5494
  _V1_MARKET_ADANUARS._serialized_start=5497
  _V1_MARKET_ADANUARS._serialized_end=5685
  _V1_MARKET_BNBNUARS._serialized_start=5688
  _V1_MARKET_BNBNUARS._serialized_end=5876
  _V1_MARKET_BTCNUARS._serialized_start=5879
  _V1_MARKET_BTCNUARS._serialized_end=6067
  _V1_MARKET_DAINUARS._serialized_start=6070
  _V1_MARKET_DAINUARS._serialized_end=6258
  _V1_MARKET_DOTNUARS._serialized_start=6261
  _V1_MARKET_DOTNUARS._serialized_end=6449
  _V1_MARKET_ETHNUARS._serialized_start=6452
  _V1_MARKET_ETHNUARS._serialized_end=6640
  _V1_MARKET_MATICNUARS._serialized_start=6643
  _V1_MARKET_MATICNUARS._serialized_end=6833
  _V1_MARKET_SOLNUARS._serialized_start=6836
  _V1_MARKET_SOLNUARS._serialized_end=7024
  _V1_MARKET_OBJECT._serialized_start=7027
  _V1_MARKET_OBJECT._serialized_end=8482
# @@protoc_insertion_point(module_scope)
