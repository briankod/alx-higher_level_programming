#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        max_ = None
    if a_dictionary:
        max_ = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if(a_dictionary[key] > a_dictionary[max_]):
                max_ = key
    return(max_)
