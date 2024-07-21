def pig_it(str_arg):
    new_string = ''
    lst1 = list(str_arg.split(' '))

    for elem in lst1:
        if(elem.isalnum()):
            new_string += elem[1:] + elem[:1] + "ay "
        else:
            new_string += elem +" "

    return new_string[:-1]