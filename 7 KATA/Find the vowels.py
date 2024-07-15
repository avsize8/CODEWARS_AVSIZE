def vowel_indices(word):
    return [i for i, v in enumerate(word, 1) if v in 'aeiouyAEIOUY']