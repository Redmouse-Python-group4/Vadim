s = "string;with;some;words;and;this;is;thelargestword"
print s
s = s.split(";")
tmp = 1
word = ""
for i in s:
    if len(i) > tmp:
        tmp = len(i)
        word = i
print "\n" + word.upper()