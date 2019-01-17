def soch(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return soch(n - 1, k) + soch(n - 1, k - 1)

n, k = map(int, input().split())
y = soch(n, k)
print(y)
