print "Society in XXI century"
x = int(raw_input("Input your age: "))
if x >= 0 and x < 7:
    print "You should be in Kindergarten"
elif x >= 7 and x < 18:
	print "You should go school"
elif x >= 18 and x <= 25:
    print "You should be in University"
elif x > 25 and x < 60:
    print "You should work"
elif x >= 60 and x <= 120:
    print "You can choose anything you want to do"
else:
    err = "Error! This programm only for people!\n"
    print err * 5