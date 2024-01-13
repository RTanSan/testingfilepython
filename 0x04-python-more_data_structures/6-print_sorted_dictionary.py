#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    orderedkeys = list(a_dictionary.keys())
    orderedkeys.sort()
    for key in orderedkeys:
        print(f"{key}: {a_dictionary[key]}")
