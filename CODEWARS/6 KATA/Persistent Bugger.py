def persistence(n):
    if n < 10:
        return 0 
    num_str = str(n)
    total = 1
    for i in num_str:
        total = total * int(i)
    return 1 + persistence(total)