import re
from dictnames import REGEX_PILOTS, REGEX_POSITIONS

def magic_regex(alist, username):
    result = []
    for message in alist:
        for regex in REGEX_PILOTS:
            captured = re.findall(regex, message)
            if captured:
                captured = captured[0].lower()
                position = ''
                for r in REGEX_POSITIONS:
                    position = re.findall(r, message)
                    if position:
                        position = position[0].lower()
                        break
                print('REG: USERNAME: {} voted: {} FOR: {}'.format(username, captured, position))
                result.append({'username': username, 'position': position, 'pilot_name': captured})
    return result
