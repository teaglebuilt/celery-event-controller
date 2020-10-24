
SRC = src
PROTOC = python -m grpc_tools.protoc
PROTOS = $(SRC)/protos
compile:
	pip-compile --output-file requirements.txt requirements.in

proto:
	$(PROTOC) --proto_path=$(SRC) --python_out=$(SRC) --grpc_python_out=$(SRC) $(PROTOS)/celery_controller.proto
	sed -i '' 's/^from protos import/from . import/' $(PROTOS)/celery_controller_grpc.py

clean: clean-build clean-pyc

clean-build:
	rm -rf build dist

clean-pyc:
	find . -type f -name *.pyc -delete
	
clean-protos:
	rm -f $(PROTOS)/*_pb2.py $(PROTOS)/*_pb2_grpc.py

build-python: clean
	python setup.py sdist bdist_wheel

worker:
	celery -A tasks worker --loglevel=INFO