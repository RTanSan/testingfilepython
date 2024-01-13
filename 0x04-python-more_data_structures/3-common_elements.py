#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1_set = set(set_1)
    set_2_set = set(set_2)

    output = set_1_set & set_2_set
    return (output)
