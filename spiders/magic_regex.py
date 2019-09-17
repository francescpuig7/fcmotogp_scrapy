import re
from dictnames import REGEX_PILOTS, REGEX_POSITIONS

def magic_regex(alist, username):
    result = []
    for message in alist:
        for regex in REGEX_PILOTS.keys():
            captured = re.findall(regex, message)
            if captured:
                captured = REGEX_PILOTS[regex].lower()
                position = '?'
                for r in REGEX_POSITIONS.keys():
                    position = re.findall(r, message)
                    if position:
                        position = REGEX_POSITIONS[r].lower()
                        break
                    else:
                        position = '?'
                print('REG: USERNAME: {} voted: {} FOR: {}'.format(username, captured, position))
                result.append({'username': username, 'position': position, 'pilot_name': captured})
    return result
