#!/usr/bin/python3
def no_c(my_string):
    list_my_string = list(my_string)
    idx_count = 0

    for i in list_my_string:
        if i == 'c' or i == 'C':
            list_my_string[idx_count] = ""
        idx_count += 1
    return "".join(list_my_string)
