import re
from dictnames import REGEX_PILOTS, REGEX_POSITIONS

def magic_regex(alist, username):
    for message in alist:
        for regex in REGEX_PILOTS:
            captured = re.findall(regex, message)
            if captured:
                for r in REGEX_POSITIONS:
                    position = re.findall(r, message)
                    if position:
                        continue
                print('REG: USERNAME: {} voted: {}'.format(username, captured))
