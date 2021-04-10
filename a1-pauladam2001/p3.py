#
# Implement the program to solve the problem statement from the third set here
#
# Ex. 13

def number_divided_by_d(nr,d):
    sem = 0
    while nr % d == 0:
                nr = nr // d
                sem = 1
    return nr, sem

def prime_factors(nr,d,ct):
    while nr > 1:
            nr,sem=number_divided_by_d(nr,d)
            if sem == 1:
                ct = ct + 1
            if ct == n:
                return ct, d
            d = d + 1
    return ct, d

def nthElem(n):
    ct = 1
    x = 2
    if n == 1:
        return 1
    while ct < n:
        nr = x
        d = 2
        ct, d = prime_factors(nr,d,ct)
        if ct == n:
            return d
        x = x + 1

n = int(input("Value: "))
print(nthElem(n))
