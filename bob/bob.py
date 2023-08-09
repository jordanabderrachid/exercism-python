import re

def response(hey_bob):
    is_silence = hey_bob.strip() == ""
    if is_silence:
        return "Fine. Be that way!"

    is_question = hey_bob.rstrip()[-1] == "?"
    is_yelling = re.search(r'[A-Z]', hey_bob) and not re.search(r'[a-z]', hey_bob)

    if is_question:
        if is_yelling:
            return "Calm down, I know what I'm doing!"
        else: 
            return "Sure."
    
    if is_yelling:
        return "Whoa, chill out!"

    return "Whatever."
