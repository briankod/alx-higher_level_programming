#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    my_list = list_of_integers
    if my_list == []:
        return None
    n = len(my_list)
    start, final = 0, n - 1
    while start < final:
        mid = start + (final - start) // 2
        if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
            return (my_list[mid])
        if my_list[mid - 1] > my_list[mid + 1]:
            final = mid
        else:
            start = mid + 1
    return (my_list[start])
