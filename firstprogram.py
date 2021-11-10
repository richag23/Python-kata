# Write a function named numbers.
#
# function should return True if all the parameters it is passed are of the integer type or float type. Otherwise,
# the function should return False.
#
# The function should accept any number of parameters.
#
# Example usage:
#
# numbers(1, 4, 3, 2, 5); # True
# numbers(1, "a", 3); # False
# numbers(1, 3, None); # False
# numbers(1.23, 5.6, 3.2) # True
def numbers(*args):
    finalResult=True
    for x in args:
        if type(x)!=int and type(x)!=float:
            finalResult=False
            return finalResult
        else:
            finalResult=True
    return finalResult

print(numbers(1, 4, 3, 2, 5))
print(numbers(1, "a", 3))
print(numbers(1, 3, None))
print(numbers(1.23, 5.6, 3.2))
                    