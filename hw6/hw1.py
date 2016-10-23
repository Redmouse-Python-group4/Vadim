from abc import ABCMeta, abstractmethod, abstractproperty
# Abstract Class
class Abstract_Input():
    __metaclass__ = ABCMeta

    @abstractproperty
    def val():
        """Value"""
# Class with all functions
class Input(Abstract_Input):
    def val(self, x):
        if 1 <= x <= 3:
            self.if1(x)
        elif x <= 6:
            self.if2(x)
        elif x <= 9:
            self.if3(x)
        else:
            print "ERROR!"
    
    def if1(self, x):
        s = raw_input("Input string: ")
        n = int(raw_input("Input repeats: "))
        i = 0
        while i < n:
            print s
            i = i + 1
    
    def if2(self, x):
        y = int(raw_input('Input number of degree: '))
        print x**y
    
    def if3(self, x):
        res = []
        for i in range(0, 10):
            x = x + 1
            res.append(x)
        for i in res:
            print i

# Final class
class Input_x(Input, Abstract_Input):
    def __init__(self, x):
        self.x = x
        self.val(self.x)


x = Input_x(int(raw_input("Input any nubmer from 1 to 9: ")))