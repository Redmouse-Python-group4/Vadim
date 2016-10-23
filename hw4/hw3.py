import random

answers = ["YES", "NO", "MAYBE", "ASK AGAIN PLEASE", "OFCOURSE",
 "I dont think so", "Do what you want to do", "Strange question...Ofcourse NO!", "Yes, if you really want it"]
print "Enter 'exit' to close this program\n"
x = True
i = 0
while x:
    question = raw_input("Enter your question: ")
    if question != "exit":
        if i == 2:
            print "***DON`T FORGET***: Enter 'exit' to close this program\n"
            i = -5
        print question + " - " + random.choice(answers) + "\n"
        i = i + 1
    else:
        x = False