#!/usr/bin/bash
def multiple_returns(sentence):
    if len(sentence) == 0:
        return ("None", 0)
    else:
        w_len = len(sentence)
        return (sentence[0], w_len)
