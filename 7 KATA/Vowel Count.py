def get_count(sentence):
    return sum(1 for i in sentence if i in "aeiouAEIOU")