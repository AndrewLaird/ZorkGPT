import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
original_prompt = ""
with open("zork_prompt.prompt", "r") as zork_prompt_file:
    original_prompt = zork_prompt_file.read()
assert original_prompt != ""

def run_openai_api(text):
    prompt = original_prompt + "\n" + text.strip("\n")
    result = openai.Completion.create(
      model="text-curie-001",
      prompt=prompt,
      max_tokens=10,
      temperature=0.7
    )
    with open("openai_api_responses.txt","w+") as f:
        f.write(str(result))
    return result['choices'][0]['text'].strip(" \n.")
