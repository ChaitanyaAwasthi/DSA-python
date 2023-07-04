# factorial 


def factorial(n):
    # define a base-case 
    if n == 1:
        return 1
    return n * factorial(n-1)

    """
    5 * 4 * 3 * 2 * 1 = 120"""

print(factorial(5))