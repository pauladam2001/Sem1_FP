#
# Implement the program to solve the problem statement from the first set here
#
# Ex. 4

def sort(a,i):
    for k in range(0,i-1):
        for j in range(k+1,i):
            if a[k] < a[j]:
                aux = a[k]
                a[k] = a[j]
                a[j] = aux

def form_number(a,i):
    m=0
    for k in range (0, i):
        m = m * 10 + a[k] 
    return m

def largestNumber(n):
    i = 0
    a = [0] * 100
    while n != 0:
        a[i] = n % 10
        i = i + 1
        n = n // 10
    sort(a,i)
    return form_number(a,i)

n = int(input("Value: "))
print(largestNumber(n))

