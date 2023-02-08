import subprocess
import time
from utils import remove_control_characters

zork_process_output_file = open("zorkOutput.txt", "w")
class Zork:
    def __init__(self,):
        self.zork_process_output_file = open("zorkOutput.txt", "w")
        self.zork_process_output_file = open("zorkOutput.txt", "r")
        self.zork_process = subprocess.Popen("./run_zork.sh", stdin=subprocess.PIPE, shell=True, stdout=zork_process_output_file, stderr=None)

    def step(self, input_str: str) -> str:
        self.zork_process.stdin.write(bytes(input_str+"\n","utf-8"))
        self.zork_process.stdin.flush()
        time.sleep(.1)
        return self.read()

    def read(self) -> str:
        self.zork_process_output_file.seek(0)
        output = self.zork_process_output_file.read()
        output = remove_control_characters(output)
        with open("zork_readable.txt","w+") as f:
            f.write(output)
        return output

if __name__ == "__main__":
    zork_process = Zork()
    output = zork_process.step("look")
    print(output)
    output = zork_process.step("open mailbox")
    print('-----------') 
    print(output)

    with open("test.txt","w+") as f:
        f.write(output)
