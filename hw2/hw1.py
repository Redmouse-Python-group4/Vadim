s = raw_input('Input your sentence: ')
print s
tmp = 1
word = ""
s = s.split()
for i in s:
    if len(i) > tmp:
        tmp = len(i)
        word = i
print "\nThe largest word is " + word.upper()

