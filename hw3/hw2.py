def if1(x, y):
    i = 0
    while i < y:
        print x
        i = i + 1

def if2(x, y):
    print x**y
    
def if3(x):
    res = []
    for i in range(0, 10):
        x = x + 1
        res.append(x)
    for i in res:
        print i

x = int(raw_input("Input any nubmer from 1 to 9: "))
if x > 0 and x < 4:
    s = raw_input("Input string: ")
    n = int(raw_input("Input repeats: "))
    if1(s, n)
elif x > 3 and x < 7:
    m = int(raw_input("Input number of degree: "))
    if2(x, m)
elif x > 6 and x < 10:
    if3(x)
else:
    print "ERROR!"