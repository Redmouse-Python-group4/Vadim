from datetime import datetime, time

date = raw_input("Input your date in dd.mm.yyyy format: ")
date = datetime.strptime(date, "%d.%m.%Y")
print date.strftime("%B %d, %y")
