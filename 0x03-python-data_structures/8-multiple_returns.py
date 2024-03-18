def multiple_returns(sentence):
    """Return a tuple with the length of a string and its 1st character"""
    if sentence:
        return len(sentence), sentence[0]
    else:
        return len(sentence), None
