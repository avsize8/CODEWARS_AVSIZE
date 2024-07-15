from functools import *
def multiply(x,y):
    return x*y
def multi(l_st):
    return reduce(multiply,l_st,1)
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]