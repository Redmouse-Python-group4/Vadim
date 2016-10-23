def length_of_word(s):
    sen = s.split()
    for i in sen:
        print i + " - " + str(len(i))

s = raw_input("Input the sentence: ")
length_of_word(s)