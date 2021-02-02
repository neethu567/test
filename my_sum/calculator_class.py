from my_sum.calculator import *
class Calculator:

    def __init__(self):
        self._number=0

    @property
    def number(self):
        return self._number

    def calculate(self,func,a,b):

        self._number=func(a,b)
        return self._number

    # def add(self,a,b):
    #     return self.calculate(add,a,b)
    #
    # def sub(self, a, b):
    #     return self.calculate(sub, a, b)
    #
    # def mul(self, a, b):
    #     return self.calculate(mul, a, b)
    #
    # def div(self, a, b):
    #     return self.calculate(div, a, b)

s1=Calculator()
print(s1._number)
print(s1.calculate(add,3,6))
print(s1.calculate(sub,3,6))
print(s1.calculate(mul,3,6))
print(s1.calculate(div,3,6))



