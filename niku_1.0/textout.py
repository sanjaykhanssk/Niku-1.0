import subprocess as subp
import os
import time
def startread():

    data = os.popen('xsel').read()
    # print(data)
    return(data)
