import findsup

f = open("price.csv", 'r')
supplies = findsup.find_supl(f)
f.close()

f = open("price.csv", 'a')
f.write("Items;%s\nPairs;%s"%(supplies[0], supplies[1]))
f.close()