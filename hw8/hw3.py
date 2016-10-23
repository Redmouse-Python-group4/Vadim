from datetime import datetime

date = "14/11/1996"
date = datetime.strptime(date, "%d/%m/%Y").date()
print date