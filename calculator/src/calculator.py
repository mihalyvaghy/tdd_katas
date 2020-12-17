import re

def find_delimiter(numbers):
    if len(numbers) > 0:
        if re.match("//(?P<delimiter>.)\n\d+(?:(?P=delimiter)\d+)*", numbers):
            return numbers[2], numbers[4:]
        else:
            return ",", numbers
    else:
        return "_", "0"

def split_numbers(numbers):
    delimiter, numbers = find_delimiter(numbers)
    return [int(number) for number in re.split(delimiter + "|\n", numbers)]

def find_negative_numbers(numbers):
    return [number for number in numbers if number < 0]

def raise_negative_numbers_error(numbers):
    raise Exception("Negative numbers not allowed", *numbers)

def add(numbers):
    numbers = split_numbers(numbers)
    if len(negative_numbers := find_negative_numbers(numbers)) > 0:
        raise_negative_numbers_error(negative_numbers)
    return sum(numbers)
