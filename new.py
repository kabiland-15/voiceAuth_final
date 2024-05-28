def swap(lst: list) -> int:
    count = 0
    for i in range((n//2)-1, 0, -1):
        if lst[i]-1 == lst[i-1] and lst[i]>lst[i-1]:
            continue
        else:
            count += 1
            

    return count

lst = [1, 2, 3, 3, 2, 1]
n = len(lst)
if n%2 == 0:
    count1 = swap(lst[:(n//2)-1])
    count2 = swap(lst[(n//2):])
    if min(count1, count2) == count1:
        lst[(n//2)-1] = lst[n//2]
        print(swap(lst))
