#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    i = 0
    while(i < len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return(my_list)
        elif i == idx:
            del my_list[i]
            new_list = my_list
            return(new_list)
        i += 1
