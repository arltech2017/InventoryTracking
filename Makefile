PYTHON:=$(shell which python3)

TEST_DIR:=tests
SRC_DIR:=warehouse

ROOT:=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))# https://stackoverflow.com/a/23324703
SRC_DIR:=$(ROOT)$(SRC_DIR)
TEST_DIR:=$(ROOT)$(TEST_DIR)

.PHONY: test
test: test-pycodestyle
	cd $(SRC_DIR) && $(PYTHON) -m doctest $(TEST_DIR)/**

.PHONY: test-pycodestyle
test-pycodestyle:
	pycodestyle $(SRC_DIR)
