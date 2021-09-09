#! /usr/bin/python3

import datetime
import socket
import time
import sys

def infi_logger(location = "terminal"):
    hostname = socket.gethostname()
    i = 0
    while True:
        ctime = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
        logline = f"{ctime}: [{hostname}] Logging count {i}"
        if location == "terminal":
            print(logline)
        else:
            with open(location, 'a') as log_file:
                log_file.write(logline + '\n')
        time.sleep(20)
        i += 1


if __name__ == "__main__":
    try:
        infi_logger("/var/log/demoLogger/logs")
    except KeyboardInterrupt:
        print("Stopping the demoLogger.")
        sys.exit(0)
    except Exception as err:
        print(err)
        sys.exit(1)