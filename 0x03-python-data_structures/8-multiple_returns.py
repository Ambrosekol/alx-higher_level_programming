#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return ("None", 0)
    else:
        w_len = len(sentence)
        return (w_len, sentence[0])
