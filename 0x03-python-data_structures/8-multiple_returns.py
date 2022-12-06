#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    first_char = sentence[0]

    if len_sentence == 0:
        new_tuple = (len_sentence, None)
    else:
        new_tuple = (len_sentence, first_char)
    
    return new_tuple
