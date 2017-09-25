PYTHON:=$(shell which python3)

TEST_DIR:=tests
SRC_DIR:=warehouse
VENV_DIR:=venv

ROOT:=$(dir $(realpath $(lastword $(MAKEFILE_LIST))))# https://stackoverflow.com/a/23324703
SRC_DIR:=$(ROOT)$(SRC_DIR)
TEST_DIR:=$(ROOT)$(TEST_DIR)
VENV_DIR:=$(ROOT)$(VENV_DIR)

.PHONY: test
test:
	cd $(SRC_DIR) && $(PYTHON) -m doctest $(TEST_DIR)/**

.PHONY: test-pycodestyle
test-pycodestyle:
	pycodestyle $(SRC_DIR)

venv:
	virtualenv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -U pip
	$(VENV_DIR)/bin/pip install -Ur requirements.txt
