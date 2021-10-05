def square(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError('Given number is greater than 64 or smaller than 0!')
    return 2 ** (integer_number - 1)


def total():
    
    sum = 0
    for i in range(1, 64 + 1):
        sum += square(i)
    return sum