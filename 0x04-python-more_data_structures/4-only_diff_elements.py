#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    n2 = set_2 - set_1
    n1 = set_1 - set_2
    n = n2 ^ n1
    return(n)
