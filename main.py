import sys
from lib import *

if (len(sys.argv) > 1) and (sys.argv[1] == 'test'):
        import os 
        import doctest
        tests = os.listdir("tests/")
        for file in tests:
            doctest.testfile("tests/{}".format(file))
