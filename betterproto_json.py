from betterproto_compiled import RootMessage, RootMessageNestedMessage
from pprint import pprint

message = RootMessage(
    int_value=10,
    nested_message=RootMessageNestedMessage(float_value=3.14),
    non_optional_field=5,
    # note that optional_field is not set
)

print("Including default values: True")
pprint(message.to_dict(include_default_values=True))

print()
print("Including default values: False")
pprint(message.to_dict(include_default_values=False))
