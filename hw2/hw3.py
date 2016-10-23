s = ["sad", "bad", "great", "salad", 'no']
sign = raw_input("Input the sign: ")
tmp = 10000
word = ""
for i in s:
    j = str(i)
    if len(j) < tmp:
        tmp = len(j)
        word = "'" + j + "'"
s = sign.join(s)
print s
print "The minimum word is " + word + "."
