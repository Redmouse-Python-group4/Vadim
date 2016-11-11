import findsup


# Open file
f = open('Pricelist.txt', 'r')
supplies = findsup.find_supl(f)
f.close()
# Write the result
f = open("Pricelist.txt", 'a')
f.write("\n%s\nItems: %s\nPairs: %s"%("-"*50, supplies[0], supplies[1]))
f.close()




