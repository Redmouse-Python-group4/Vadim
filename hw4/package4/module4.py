def if1(x, y):
    i = 0
    while i < y:
        print x
        i = i + 1

def if2(x, y):
    print x**y
    
def if3(x):
    res = [i for i in range(x + 1, x + 11)]
    for i in res:
        print i
