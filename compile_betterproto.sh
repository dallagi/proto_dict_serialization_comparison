#!/bin/sh

mkdir betterproto_compiled 2>/dev/null || true
python -m grpc_tools.protoc --proto_path=. --python_betterproto_out=betterproto_compiled example.proto
