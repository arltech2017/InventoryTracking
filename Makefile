PYTHON:=$(shell which python3)
ROOT:=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))# https://stackoverflow.com/a/23324703
TEST_DIR:=tests
SRC_DIR:=src

SRC_DIR:=$(ROOT)/$(SRC_DIR)
TEST_DIR:=$(ROOT)/$(TEST_DIR)

test:
	cd $(SRC_DIR) && $(PYTHON) -m doctest $(TEST_DIR)/**

