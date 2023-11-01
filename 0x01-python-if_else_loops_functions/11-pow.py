#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
        else:
            for _ in range(-b):
                result /= a
        formatted_result = "{:.15e}".format(result)
    return float(formatted_result)
