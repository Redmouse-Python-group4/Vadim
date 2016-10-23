s = str(raw_input("Input the sentence: "))
n = s.split()
if len(n) == 1:
    print "Your sentence consist of " + str(len(n)) + " word."
else:    
    print "Your sentence consist of " + str(len(n)) + " words."