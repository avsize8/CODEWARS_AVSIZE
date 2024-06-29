def filter_list(l):
    result = []
    l = list(l)
    for element in l:
        if element != str(element):
            result.append(element)
    return result