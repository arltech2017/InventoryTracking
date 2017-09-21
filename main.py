#!/usr/bin/env python3.6
# coding=utf-8
import sys

if (len(sys.argv) > 1) and (sys.argv[1] == 'test'):
        import os 
        import doctest
        tests = os.listdir("tests/")
        for test_file in tests:
            doctest.testfile("tests/{}".format(test_file))
