def find_outlier(integers):
    even_list = [n for n in integers if n % 2 == 0]
    odd_list = [n for n in integers if n % 2 == 1]
    if len(even_list) == 1:
        return even_list[0]
    elif len(odd_list) == 1:
        return odd_list[0]