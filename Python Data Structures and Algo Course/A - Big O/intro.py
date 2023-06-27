# space complexity - memory space measure
# time complexity - measured by no of operations

# array = [1, 2, 3, 4, 5]
# extracting 1 would be the best case scenario
# exactring 3 would be the avg
# extracting 5 would be the worst case scenario
# omega - best case scenerio
# theta - avg case scenario
# Big O - worst case scenario

# big O proportional - O(n) # linear time complexity

# example of O(n)

def print_items(x):
    for i in range(x):
        print(i)


# As it linearlly extracts every single item, the time complexity is proportional to the items.. O(n)
print_items(10)

"""simplifying big O"""
"""dropping constants"""

# this has the same for loop written twice, which means the whole array gets iterated twice/
# - does that mean the running time compelxity is O(n+n) --> O(2n) in the world or Big O
# you can drop the constants as it does not affect the time complexity and write it as 0(n)\


def print_item(y):
    for i in range(y):
        print(i)

    for i in range(y):
        print(i)


print_item(10)

# why do we not care about the constants in big O notation

"""Big-O notation doesn't care about constants because big-O notation only describes the long-term growth rate of functions,
 rather than their absolute magnitudes. Multiplying a function by a constant only influences its growth rate by a constant 
 amount, so linear functions still grow linearly, logarithmic functions still grow logarithmically, exponential functions
   still grow exponentially, etc. Since these categories aren't affected by constants, it doesn't matter that we drop the 
   constants."""


def print_item(y):
    for i in range(y):
        for j in range(y):
            print(i, j)


# this will return as how a nested loop returns
# in total we have 100 items printed out
# which is basically n*n = n**2
print_item(10)
# the graph is much steeper which means that it's less efficient

"""Another simplification technique - Drop Non-Dominants"""


def print_item(y):
    for i in range(y):
        for j in range(y):
            print(i, j)

    for k in range(y):
        print(k)


print_item(10)

# if we use this the time complexity becomes -- 0(n**2 + n) (n**2 because of the nested loop, and n became of extra for loop)
# so when we calculate n**2 for example n = 100 n**2 becomes 100,000
# and if we take n which is just 100, the % of n to n**2 becomes insignificant

"""constant running time complexity O(1)"""


def add_items(n):
    return n + n

# Time complexity is the measure of no of operaitons
# So in this case the no of operations is only equal to 1 as-
# we are only adding n and it doesn't matter if we add n + n + n + n....nm times the 1 operation remains constant


"""O(Logn) running time complexity"""

array = [1, 2, 3, 4, 5, 6, 7, 8]
# if we want to find 1

# we can divide the array 1/2
# we select this as we want to find one and after 1/2 it one is in this sub-array
array_half = [1, 2, 3, 4]
array_half_half = [1, 2]
array_3half = [1]  # we found 1 by halving

# how mnay operations did it take ?
# IT took 3 operations

# And 2**3 = 8 (8 is the total number of items)
# we can also right this as log(base)2 (8) = 3
# intuitively we are deviding the 8 array by 2 in which operations are 3


"""log_base2_8 = you're basically saying that 2 to the what power is equal to 8, 2**x = 8 find x ???"""

# on the graph O(log n) is very close to constant running time complexity

"""O(nlog n)"""
# used for sorting algorithms

# in which first you divide the array into halves which takes the logn
# then you merge these sublists of division and combine them ( you sort them by comparing the sublists)


def print_items(a, b):
    for item in range(a):
        print(item)
    for element in range(b):
        print(element)


print_items(10, 15)

# now the time complexity will not be O(n + n) as you are taking two different parameters
# people will think that for loop is f(n) and two for loops are On + n) = O(2n) drop the constant - f(n)
# but in this case the running time complexity will be O(a + b


def print_items(a, b):
    for item in range(a):
        for element in range(b):
            print(item, element)


print_items(10, 15)

# if there is a nested loop then the running time complexity will be O(a * b)
