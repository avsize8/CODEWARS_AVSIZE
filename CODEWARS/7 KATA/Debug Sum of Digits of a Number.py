def get_sum_of_digits(num):
    exit = 0
    digits = list(str(num))
    for x in digits:
        exit += int(x)
    return exit