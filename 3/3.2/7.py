s = input()
t = input()
n = 0
m = 0
print(len(s))
print(t)

while len(s) > n+1:
    if s.find(t, n) != -1:
        n = s.find(t, n) + 1
        m += 1
        
    else:
        n += 1

print(m)