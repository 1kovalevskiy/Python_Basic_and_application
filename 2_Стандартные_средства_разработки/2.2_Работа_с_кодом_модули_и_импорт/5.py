import datetime

a = datetime.date(2016,5,4)
b = datetime.timedelta(days=14)
c = a + b
print(c)
print(c.year, c.month, c.day)