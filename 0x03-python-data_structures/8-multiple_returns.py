#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]

    if length == 0:
        new_tuple = (length, None)
    else:
        new_tuple = (length, first_char)
    return (new_tuple)
