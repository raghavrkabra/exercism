def response(hey_bob):
    """How bob respond when you say him someting."""
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


# Bob has only a few responses which are listed here
_responses = ["Fine. Be that way!",  # for silence
              "Calm down, I know what I'm doing!",  # for shouted question
              "Sure.",  # for question (in normal tone)
              "Whoa, chill out!",  # for something shouted
              "Whatever."  # default response
              ]


def _is_question(sentence: str) -> str:
    return sentence.endswith("?")


def _is_shouting(sentence: str) -> str:
    return sentence.isupper()


def _is_silence(sentence: str) -> str:
    return sentence == ""
