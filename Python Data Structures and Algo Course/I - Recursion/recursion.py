# Base Case - the function will stop calling itself 
# Recursive Case - the function will keep calling itself 
# this unlimited loop is known as - stack overflow 
# we also need a return statement...if we use print() then it will just print and loop
# return stops the code 

"""call stack"""


def funcThree():
    print(3)

def funcTwo():
    funcThree()
    print(2)

def funcOne():
    funcTwo()
    print(1)

funcOne()




