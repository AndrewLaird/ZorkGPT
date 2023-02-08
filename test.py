import re
import unicodedata
with open("zorkOutput.txt", "r") as f:
    string = f.read()
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    result = ansi_escape.sub('', string)
    string = ansi_escape.sub('', string)
    for s in string:
        print(s,unicodedata.category(s))
    print(string)
    
