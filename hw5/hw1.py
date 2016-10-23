class Input():
    def __init__(self, x):
        self.x = x
        if 1 <= self.x <= 3:
            self.if1(self.x)
        elif self.x <= 6:
            self.if2(self.x)
        elif self.x <= 9:
            self.if3(self.x)
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
        res = [i for i in range(x + 1, x + 11)]
        for i in res:
            print i

x = Input(int(raw_input("Input any nubmer from 1 to 9: ")))