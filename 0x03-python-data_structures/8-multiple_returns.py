#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None
    for i in sentence:
        if length == 0:
            first_char = i
        length += 1
    return_tuple = (length, first_char)
    return (return_tuple)
'''    len_sentence = len(sentence)
    first_char = sentence[0]

    if len_sentence == 0:
        new_tuple = (len_sentence, None)
    else:
        new_tuple = (len_sentence, first_char)

    return new_tuple'''
