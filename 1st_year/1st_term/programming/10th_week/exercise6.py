from typing import AsyncIterable

def count_mine(arg, x):
    aux = 0

    for i in arg:
        if(i == arg):
            aux += 1

    return aux

def index(arg, x):
    aux = 0

    for i in arg:
        if(i == arg):
            return aux

        aux += 1

def append_mine(arg, x):
    return arg + [x]

#My approach is to copy the arrray until the index and delete those elements from the original list
#Then return the auxiliar list adding the x element as a list and the final part of the array
def insert_mine(arg, x, index):
    aux_ls, aux_int= [], 0

    while (aux_int != index):
        aux_ls += [arg[0]]
        aux_int += 1
        del arg [0]

        arg = aux_ls + [x] + arg

        return aux_ls + [x] + arg

def remove_mine(arg, x):
    aux = 0

    while(arg[aux] != x and aux < len(arg)):
        aux += 1

    if(arg[aux] == x):
        del arg[aux]

    return arg

def removeAll_mine(arg, x):
    aux_ls = []
    for i in arg:
        if(i != x):
            aux_ls += [i]

    return aux_ls

def clear_mine(arg):
    arg = []
    return []

def pop_mine(arg):
    aux = arg[len(arg) - 1]
    del arg[len(arg) - 1]
    return aux

l = [1,2,34,6]
a = pop_mine(l)
print(a)