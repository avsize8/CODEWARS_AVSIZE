def disemvowel(string):
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])