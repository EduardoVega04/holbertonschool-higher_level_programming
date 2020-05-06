#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i in s:
        if i in "cC":
            s.remove(i)
    my_string = "".join(s)
    return (my_string)
