from datetime import datetime, timedelta
# Find date function
def day_number(x, year):
		# Enter day number
		n = int(raw_input("Enter your day number(your number should be in range (1, %s)): "%x))
		# Find date
		date = datetime(year, 1, 1) + timedelta(n - 1)
		# Check on correct day number
		if 1 <= n <= x:
			print date.strftime("Month: %B\nDay: %d")
		else:
			print "Your number should be in range (1, %s)!" %(x)
			day_number(x, year)
# Is it leap year or no function
def check_leap_year():
	# Ask about leap year
	l_y = raw_input("Is it leap year? Enter 'yes' or 'no': ")
	if l_y == 'yes':
		# For leap year
		day_number(366, 2016)
	elif l_y == 'no':
		# For not leap year
		day_number(365, 2015)
	else:
		# Error in case of incorrect answer
		print "Please enter 'yes' or 'no'!"
		check_leap_year()

check_leap_year()