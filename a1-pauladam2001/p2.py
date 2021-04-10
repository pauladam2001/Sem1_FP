#
# Implement the program to solve the problem statement from the second set here
#
# Ex. 10
def palindrome(n):
    pal = 0
    while n > 0:
        pal = pal * 10 + n % 10
        n = n // 10
    return pal

n = int(input("Value: "))
print(palindrome(n))