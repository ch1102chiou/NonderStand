import sys
import os
import inspect

t = os.path.dirname(os.path.realpath(__file__))
DEBUG = True
DEVELOPEMENT = False



if DEBUG is True:
    t = t + "/test.in" 
    testfile = open(t)    

def getLine():
    if DEBUG:
        tmp = next(testfile)
        while tmp.startswith("#"):
            tmp = next(testfile)
            continue
        print("CMD: %s" %(tmp))
        return tmp
    elif DEVELOPEMENT is True:
        tmp = sys.stdin.readline()
        return tmp

