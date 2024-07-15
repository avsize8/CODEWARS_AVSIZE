def narcissistic( value ):
    total = 0
    num = str(value)
    for digit in num:
        total += int(digit)**len(num)
    return total == value