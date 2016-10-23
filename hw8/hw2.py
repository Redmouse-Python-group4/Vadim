from datetime import datetime
day = 5
month = 9
year = 2016
date = datetime.strptime(str(year) + str(month) + str(day), "%Y%m%d").date()
print date