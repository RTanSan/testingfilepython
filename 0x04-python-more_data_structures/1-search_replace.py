#!/usr/bin/python3
def search_replace(my_list, search, replace):
    seen_elements = set([])
    for idx, ele in enumerate(my_list):
        if ele == search and ele not in seen_elements:
            my_list[idx] = replace
            seen_elements.add(ele)
            return (my_list)
