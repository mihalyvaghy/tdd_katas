def roman_to_decimal(roman):
    lut = {
            "I":    1,
            "V":    5,
            "X":   10,
            "L":   50,
            "C":  100,
            "D":  500,
            "M": 1000
            }

    value = 0
    for i in range(len(roman)-1):
        if lut[roman[i+1]] <= (cur_number := lut[roman[i]]):
            value += cur_number
        else:
            value -= cur_number
    value += lut[roman[-1]]
    return value
