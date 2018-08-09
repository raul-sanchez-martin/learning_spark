import os
import time
import signal

if __name__ == "__main__":
    
    lines = list(open('../data/error_log.txt').readlines())
    
    with open("../data/error_log.txt") as f:
        for line in f.readlines():
            line = line.strip()
            print("Sending message: {0}".format(line))
            command = "echo '{0}' | nc -q 1 -lp 9999 127.0.0.1".format(line)
            os.system(command)