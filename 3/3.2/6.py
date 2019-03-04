s = input()
a = input()
b = input()
n = 0

while s.find(a) != -1 and n < 1001:
    s = s.replace(a,b)
    n += 1


if n >= 1000:
    print("Impossible")
 
else:
    print(n)