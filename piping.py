# import subprocess

# bash_script = "frotz zork1.z5"

# process = subprocess.Popen(["frotz", "zork1.z5"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# print(process.stdout.readline().decode())
# input_data = b"open leaflet\n"
# process.stdin.write(input_data)
# process.stdin.flush()

# print(process.stdout.readline().decode())


import subprocess
import time
import re
from termcolor import colored

import unicodedata

def remove_control_characters(text):
    # 7-bit C1 ANSI sequences
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    # ansi_escape = re.compile(r'''
        # \x1B  # ESC
        # (?:   # 7-bit C1 Fe (except CSI)
            # [@-Z\\-_]
        # |     # or [ for CSI, followed by a control sequence
            # \[
            # [0-?]*  # Parameter bytes
            # [ -/]*  # Intermediate bytes
            # [@-~]   # Final byte
        # )
    # ''', re.VERBOSE)
    result = ansi_escape.sub('', text)
    if(result != text):
        print("different")
    to_remove = ['']
    # result = "".join(x for x in result if x not in to_remove)
    # remove_escaped_sequences =re.compile(r'(\x9B|\x1B|\[)(?:.*)\b')
    # result = remove_escaped_sequences.sub('', result)
    return result

# Open the output file in write mode
# with open("output.txt", "w") as f:
    # # Start the subprocess and redirect its stdout to the output file
    # process = subprocess.Popen(["command"], stdout=f)

    # # Wait for the subprocess to start
    # time.sleep(1)

    # # Open the output file in read mode
    # with open("output.txt", "r") as output_file:
        # # Read the contents of the output file
        # print(output_file.read())

# Start the Frotz zork_process process
# Open the output file in write mode
f = open("zorkOutput.txt", "w")

zork_process = subprocess.Popen("./run_zork.sh", stdin=subprocess.PIPE, shell=True, stdout=f, stderr=subprocess.PIPE)

# Wait for the subprocess to start
time.sleep(1)




# Send a command to the zork_process
for i in range(10):
    zork_process.stdin.write(b'look\n')
    time.sleep(.1)
    zork_process.stdin.flush()
    time.sleep(.5)

# Read the zork_process's output
time.sleep(.1)

print("hi")
f_read = open("zorkOutput.txt", "r")
print("hi2")
output_string = remove_control_characters(colored(f_read.read(), 'red'))
print(output_string)
print("hi3")

with open("helloOutput.txt", "w") as f_write:
    f_write.write(output_string)
    f_write.flush()



# bash_script = "./easy.sh"

# # create the subprocess
# process = subprocess.Popen(bash_script, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# for i in [1, 2, 3]:
    # # send input to the process
    # process.stdin.write(str(i).encode() + b'\n')
    # process.stdin.flush()
    # #print the output
    # print(process.stdout.readline().decode())

# zork_process.kill()
