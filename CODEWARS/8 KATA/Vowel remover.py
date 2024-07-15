def shortcut( s ):
    vowels = ('a', 'e', 'i', 'o', 'u')
    ss = ""
    for c in s:
        if c not in vowels:
            ss += c
    return ss