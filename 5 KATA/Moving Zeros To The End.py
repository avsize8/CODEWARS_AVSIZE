def move_zeros(array):
    zero = []
    new = []
    n = len(array)
    for i in range(n):
        if array[i] != 0:
            new.append(array[i])
        else:
            zero.append(array[i])
    array = new + zero
    return array