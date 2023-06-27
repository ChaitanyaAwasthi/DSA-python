# num 1 is pointing towards 11
num1 = 11
num2 = num1


"""integers are immutable, you can't change a number but can change their memory id"""
"""dictionaries are mutable"""

"""when there are no pointer to a value then python will remove() it through garbage collection"""

"""for example if 
    dict 1 = {key: value}
    dict 2 = dict 1
it will just point to the key value pair of dict 1 

now if we change dict2['key'] = 23
# it will not create a new 23 but will just point towards dict 1, changing dict1 value as well. which does not change
the memory location
the old value of dict1 will be removed as there are no more pointers to it, and will get removed by python
which makes the value inACCESSIBLE
]"""
