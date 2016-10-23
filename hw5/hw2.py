print "Society in XXI century"

class Society():
    def __init__(self, x):
        self.x = x
        if 0 <= self.x < 7:
            self.if1()
        elif self.x < 18:
            self.if2()
        elif self.x <= 25:
            self.if3()
        elif self.x < 60:
            self.if4()
        elif self.x <= 120:
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

x = Society(int(raw_input("Input your age: ")))


    