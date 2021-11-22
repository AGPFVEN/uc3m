from typing import AsyncIterable


def count_mine(list1, x):
    aux = 0

    for i in list1:
        if(i == list1):
            aux += 1

    return aux

def index(list1, x):
    aux = 0

    for i in list1:
        if(i == list1):
            return aux

        aux += 1

def append_mine(list1, x):
    return list1 + [x]

#My approach is to copy the arrray until the index and delete those elements from the original list
#Then return the auxiliar list adding the x element as a list and the final part of the array
def insert_mine(list1, x, index):
    aux_ls, aux_int= [], 0

    while (aux_int != index):
        aux_ls += [list1[0]]
        aux_int += 1
        del list1 [0]

        return aux_ls + [x] + list1

def remove_mine(list1, x):
    aux = 0

    while(list1[aux] != x and aux < len(list1)):
        aux += 1

    if(list1[aux] == x):
        del list1[aux]

    return list1

def removeAll_mine(list1, x):
    aux_ls = []
    for i in list1:
        if(i != x):
            aux_ls += [i]

    return aux_ls

def clear_mine(list1):
    return []

def pop_mine(list1):
    aux = list1[len(list1) - 1]
    del list1[len(list1) - 1]
    return list1, aux