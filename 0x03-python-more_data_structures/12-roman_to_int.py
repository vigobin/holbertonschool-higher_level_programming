#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    sum = 0
    length = len(roman_string)
    for i in range(length):
        if i + 1 < length and roman_dict[roman_string[i]] <\
                roman_dict[roman_string[i + 1]]:
            sum -= roman_dict[roman_string[i]]
        else:
            sum += roman_dict[roman_string[i]]
    return sum
