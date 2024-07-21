def validate_pin(pin):
    validNums = "0123456789"
    validNumsList = list(validNums)
    pin = list(pin)
    valid = True
    if (len(pin) != 4) and (len(pin) != 6):
        valid = False
    else:
        for digit in pin:
            if digit not in validNumsList:
                valid = False
    return valid