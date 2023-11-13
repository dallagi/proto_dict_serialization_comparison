from google.protobuf.json_format import MessageToDict
from proto_compiled.example_pb2 import RootMessage
from pprint import pprint

message = RootMessage(
    int_value=10,
    nested_message=RootMessage.NestedMessage(float_value=3.14),
    non_optional_field=5,
    # note that optional_field is not set
)

print("Including default values: True")
pprint(MessageToDict(message, including_default_value_fields=True))

print()
print("Including default values: False")
pprint(MessageToDict(message, including_default_value_fields=False))
