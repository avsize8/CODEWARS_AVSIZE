def calculate(a, o, b):
    result = 0
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "/" and b != 0:
        return a / b
    if o == "/" and b == 0:
        return None
    if o != "+" and o != "-" and o != "/" and o != "*":
        return None
    if o == "*":
        return a * b
    return result
print(calculate(12,"/",0))