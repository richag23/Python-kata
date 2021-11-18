#Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.
#Triangular Numbers cannot be negative so return 0 if a negative number is given
# nth traingular number is n*(n+1)/2-- 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105
#The range() is an in-built function in Python. It returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number.
# using recursion to get some of Traingular numbers

def sum_triangular_numbers(n):
    if n < 0:
        return 0

    sum = sum_triangular_numbers(n-1)
    return sum + (n * (n + 1)) / 2


print(sum_triangular_numbers(5))
    