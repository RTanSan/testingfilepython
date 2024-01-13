#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        my_list = []
    output = sum(set(my_list))
    return (output)
    print("Result: {:d}".format(output))
