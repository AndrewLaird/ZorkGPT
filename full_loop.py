import time
from subprocess_zork import Zork
from openai_api import run_openai_api

zork = Zork()
time.sleep(.1)
context = zork.read()
def run_step():
    global context
    openai_result = run_openai_api(context)
    with open("openai_api_responses.txt","w+") as f:
        f.write(str(openai_result))
    print("Openai response:", openai_result)
    next_frame = zork.step(openai_result)
    new_response = ""
    if (next_frame[0:len(context)] == context):
        new_response = next_frame[len(context):] 
    print("zork response:", new_response)
    context = next_frame

for i in range(100):
    run_step()
    time.sleep(3)

