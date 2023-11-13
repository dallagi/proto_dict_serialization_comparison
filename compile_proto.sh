#!/env/sh

mkdir proto_compiled 2>/dev/null || true
protoc --python_out=proto_compiled example.proto
