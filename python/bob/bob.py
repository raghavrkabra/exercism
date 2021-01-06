def response(hey_bob):
    hey_bob = hey_bob.strip()

    if _is_silence(hey_bob):
        return _responses[0]
    if _is_question(hey_bob):
        if _is_shouting(hey_bob):
            return _responses[1]
        else:
            return _responses[2]
    elif _is_shouting(hey_bob):
        return _responses[3]
    else:
        return _responses[4]
    pass


_responses = ["Fine. Be that way!",
              "Calm down, I know what I'm doing!",
              "Sure.",
              "Whoa, chill out!",
              "Whatever."]


def _is_question(speech: str) -> str:
    return speech.endswith("?")


def _is_shouting(speech: str) -> str:
    return speech.isupper()


def _is_silence(speech: str) -> str:
    return speech == ""
