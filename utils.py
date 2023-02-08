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
    # remove numbers at the end of input lines
    # to_remove = ['']
    # result = "".join(x for x in result if x not in to_remove)
    # remove_escaped_sequences =re.compile(r'(\x9B|\x1B|\[)(?:.*)\b')
    # result = remove_escaped_sequences.sub('', result)
    return result



