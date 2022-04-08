from array import array
from multiprocessing.dummy import Array
import string
from unittest import result


class term:
    def __init__(self, coefficient:float, variable:string, degree:float):
        self.coefficient = coefficient
        self.variable = variable
        self.degree = degree

class Polynomial:
    def  __init__(self, coefficient:float):
        self.polynomial = [coefficient]

    def __getitem__(self, i):
        return self.polynomial[i]

    def getDegree(self):
        result = 0

        for i in self.polynomial:
            if type(i) == term:
                if i.degree > result:
                    result = i.degree
        
        return result

    def getCoefficient(self, n):
        if n >= len(self.polynomial):
            print("Not valid index")
            return None
        
        elif n == 0:
            return self.polynomial[0]

        for i in self.polynomial:
            if i.degree == n:
                return i.coefficient

term1 = term(8, "x", 2)

pol1 = Polynomial(2)
pol1.polynomial.append(term1)
print(pol1.getCoefficient(1))