#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Print up to x elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The maximum number of elements to print.

    Returns:
        The number of elements successfully printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
