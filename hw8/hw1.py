from datetime import datetime

date = 19901204
print datetime.strptime(str(date), "%Y%m%d").date()
