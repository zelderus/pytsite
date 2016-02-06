import datetime
import time


_fileName = "log.txt"


def _write(fileName, msgStr):
##    log = open(fileName, "w")
##    log.write(msgStr)
##    log.flush()
##    log.close()
    with open(fileName, "a") as lf:
        lf.write(msgStr+"\n")
        

def setup(fileName):
    global _fileName
    _fileName = fileName
    
def log(msgStr):
    global _fileName
    fn = _fileName
    _write(fn, msgStr)


def logt(msgStr):
    global _fileName
    fn = _fileName
    _write(fn, str(datetime.datetime.now()) +":"+msgStr)
