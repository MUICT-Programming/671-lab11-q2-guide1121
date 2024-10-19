# YOUR CODE HERE

n = int(input())
lst1 = []
lst2 = []

for i in range(n):
    a = int(input())
    lst1.append(a)

for i in range(n):
    a = int(input())
    lst2.append(a)



def summation(a, b):
    lst_sum = []
    global n
    for i in range(n):
        sum = a[i] + b[i]
        lst_sum.append(sum)
    return lst_sum

def find_min_max(a):
    max = a[0]
    min = a[0]
    for i in a:
        if i > max :
            max = i
        else:
            continue
    for i in a:
        if i < min :
            min = i
        else:
            continue
    min_max = (min, max)
    return min_max


lst_sum = summation(lst1, lst2)
print(summation(lst1, lst2))
print(find_min_max(lst_sum))



