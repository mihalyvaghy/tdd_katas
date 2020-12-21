def prime_factors(number):
    factors = []
    factor = 2
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number /= factor
        else:
            factor += 1
    return factors
