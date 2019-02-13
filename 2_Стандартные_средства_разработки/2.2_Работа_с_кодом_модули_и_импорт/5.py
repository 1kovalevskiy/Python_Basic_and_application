import datetime

y,m,d = map(int, input().split())
delta = int(input())
a = datetime.date(y,m,d)
b = datetime.timedelta(days=delta)
c = a + b

print(c.year, c.month, c.day)