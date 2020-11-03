import sys


def sum_digit_in_string(string):
    return sum([int(digit) for digit in string])


print(sum_digit_in_string(sys.argv[1]))
