objects = [1,2,3,1,2] #input from stepik
ans = {}
for obj in objects:
    if id(obj) not in ans:
        ans[id(obj)] = 0
print(len(ans))
