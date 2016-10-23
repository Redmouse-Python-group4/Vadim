x = int(raw_input("Input any nubmer from 1 to 9: "))
if x > 0 and x < 4:
    s = str(raw_input("Input string: "))
    n = int(raw_input("Input repeats: "))
    i = 0
    while i < n:
        i += 1
        print s
elif x > 3 and x < 7:
    m = int(raw_input("Input number of degree: "))
    print x ** m
elif x > 6 and x < 10:
    i = 0
    while i < 10:
        x += 1
        print x
        i += 1 
else:
    print "ERROR!"