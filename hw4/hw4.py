import random
import re
# Random words
words = ["red", "pepper", "salt", "pirate",
 "storm", "snow", "ice", "archive", "sold", "reverse", "bob"]
# Random number of words from 3 to 10
numb_words = random.randrange(3, 10)
# Sentence Array 
sent = list()
# Add random words into the sentence
for i in range(0 , numb_words):
    sent.append(random.choice(words))
sentence = " ".join(sent) 
print sentence
# Ask to enter word
s = raw_input("Input your word: ")
# Find the first and the last words in the sentence
result = re.findall(r'^\w+', sentence) + re.findall(r'\w+$', sentence)
# Reverse word
if s == result[0] and s == result[1]:
	w = s[::-1]
	sent[0] = w
	sent[len(sent) - 1] = w
	sentence = " ".join(sent)
	print sentence
elif s == result[0]:
	w = s[::-1]
	sent[0] = w
	sentence = " ".join(sent)
	print sentence
elif s == result[1]:
	w = s[::-1]
	sent[len(sent) - 1] = w
	sentence = " ".join(sent)
	print sentence
else:
	pass

