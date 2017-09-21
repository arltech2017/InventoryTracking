PYTHON:=$(shell which python3)
ROOT_DIR:=$(dir $(realpath $(lastword $(MAKEFILE_LIST)))) # https://stackoverflow.com/a/23324703
TEST_DIR:=$(ROOT_DIR)/tests
SRC_DIR:=$(ROOT_DIR)/tests
test:
	cd src/ && $(PYTHON) -m doctest -v ../tests/**

