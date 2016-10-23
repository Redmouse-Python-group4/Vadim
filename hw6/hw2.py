from abc import abstractproperty, ABCMeta

print "Society in XXI century"
# Abstract class
class Abstract():
    __metaclass__ = ABCMeta

    @abstractproperty
    def val():
        """Input x"""
# Class with all functions
class Society(Abstract):
    def val(self, x):
        if 0 <= x < 7:
            self.if1()
        elif x < 18:
            self.if2()
        elif x <= 25:
            self.if3()
        elif x < 60:
            self.if4()
        elif x <= 120:
            self.if5()
        else:
            self.error()

    def if1(self):
        print "You should be in Kindergarten"
    def if2(self):
        print "You should go school"
    def if3(self):
        print "You should be in University"
    def if4(self):
        print "You should work"
    def if5(self):
        print "You can choose anything you want to do"
    def error(self):
        err = "Error! This programm only for people!\n"
        print err * 5

class Input_x(Society, Abstract):
    def __init__(self, x):
        self.x = x
        self.val(self.x)
        

x = Input_x(int(raw_input("Input your age: ")))