#!/usr/bin/python3
roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(roman_string):
    # Check if the input is a string and not None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    prev_value = 0

    # Iterate over the Roman numeral string from right to left
    for char in reversed(roman_string):
        # Get the value of the current Roman numerical symbol
        current_value = roman_values.get(char, 0)

        # If the current value is less than the previous value
        # substract if from the result, otherwise add it
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value

        # Update the previous value for the next iteration
        prev_value = current_value
        return result
