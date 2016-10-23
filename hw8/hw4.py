from datetime import datetime
date = datetime.today()
date = date.replace(year = (date.year + 1), month = (date.month - 1))
print date.strftime('%Y-%m Day number:%j')
