def digitize(n):
    s = []
    for i in str(n):
        i = int(i)
        s.append(i)
    return s[::-1]