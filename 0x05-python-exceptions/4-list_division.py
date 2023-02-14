#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)

# A function that divides element by element 2 lists.
# list_length can be bigger than the length of both lists
# Returns a new list (length = list_length) with all divisions
# If 2 elements can’t be divided, the division result should be
# equal to 0
