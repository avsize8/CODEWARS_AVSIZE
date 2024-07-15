def square_digits(num):
    res = [int(x) for x in str(num)]
    new_res = [i ** 2 for i in res]
    s = "".join(str(s) for s in new_res)
    return int(s) 