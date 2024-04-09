#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
            elif my_list_2[i] == 0:
                print("division by 0")
                result.append(0)
            elif not all(isinstance(x, (int, float)) for x in [my_list_1[i], my_list_2[i]]):
                print("wrong type")
                result.append(0)
            else:
                division = my_list_1[i] / my_list_2[i]
                result.append(division)
        except IndexError:
            print("out of range")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
