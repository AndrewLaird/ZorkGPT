import select
import sys
import subprocess
from queue import Queue
import fcntl
import os


# start the bash process
bash_process = subprocess.Popen("./run_zork.sh", stdin=subprocess.PIPE, shell=True,
                                stdout=subprocess.PIPE, bufsize=0) # bufsize=0 means non blocking
# set stdin to non-blocking mode
fcntl.fcntl(bash_process.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
print('after')

# create queues for reading and writing
reading_queue = Queue()
writing_queue = Queue()

# put a number in the writing queue
next_command="open_letter"
writing_queue.put("open letter")

while True:
    # use select to check if the process is ready for reading or writing
    readable, writable, exceptional = select.select([bash_process.stdout], [bash_process.stdin], [])

    # check if the process is ready for writing
    if bash_process.stdin in writable:
        # get the number from the writing queue
        # number = writing_queue.get()
        # write the number to the process
        bash_process.stdin.write(bytes(str(next_command) + '\n', 'utf-8'))
        bash_process.stdin.flush()

    # check if the process is ready for reading
    if bash_process.stdout in readable:
        # read the output from the process
        # data = os.read(bash_process.stdout.fileno(), 100000000000)
        data = ""
        for stdout_line in iter(bash_process.stdout.readline, ""):
            data += str(stdout_line)
        # check if there is any data to read
        if data:
            # put the data in the reading queue
            reading_queue.put(data)
            # print the data
            print(data)
            break


