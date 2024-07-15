def solution(s):
    list_of_pairs = []
    pair = ''
    for char in s:
        pair += char
        if len(pair) == 2:
            list_of_pairs.append(pair)
            pair = ''
    if pair:
        list_of_pairs.append(pair + '_')
    return list_of_pairs
