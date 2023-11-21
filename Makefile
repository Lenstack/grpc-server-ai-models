PROTOC = python3 -m grpc_tools.protoc
PROTO_SRC_DIR = ./proto
PROTO_OUT_DIR = ./pkg
PROTO_INCLUDES = -I$(PROTO_SRC_DIR)
PROTO_FILES = $(wildcard $(PROTO_SRC_DIR)/*.proto)

generate_protos: $(PROTO_FILES)
	$(PROTOC) $(PROTO_INCLUDES) \
		--python_out=$(PROTO_OUT_DIR) \
		--pyi_out=$(PROTO_OUT_DIR) \
		--grpc_python_out=$(PROTO_OUT_DIR) \
		$^

$(PROTO_FILES):
	@echo "Building $@"

.PHONY: generate_protos $(PROTO_FILES)
