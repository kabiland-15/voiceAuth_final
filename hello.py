def hero(n, m, h, lst):
    for i in range(n-1, 0, -1):
        if lst[i] > h:
            return i+1

    i = 0
    while i < n and m > 0:
        if h - lst[i] == 0:
            m -= 1
            i += 1
        elif h - lst[i] > 0:
            h -= lst[i]
            i += 1
        else:
            m -= 1
            h = flag
    print(i)
    flag1 = 0
    for j in range(i, n):
        flag1 += lst[j]
    flag2 = 0
    k = 0
    while k < n:
        flag2 += lst[k]
        if flag2 >= flag1:
            break
        k += 1
    return k


n = int(input())
m = int(input())
h = int(input())
flag = h
lst = [0 for _ in range(n)]
for i in range(n):
    lst[i] = int(input())
print(hero(n, m, h, lst))
