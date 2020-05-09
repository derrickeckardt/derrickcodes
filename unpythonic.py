#!/usr/bin/env python3
import timeit
from random import randint

# Square difference
setup1 = """
from random import randint

# Generate test data set
dict1 ={}
dict2 = {}
for i in range(1000):
    dict1[i] = randint(0,255)
    dict2[i] = randint(0,255)


def method1(dict1,dict2):
    for i in range(1000):
        for j in range(1000):
            distance_squared = (dict1[i] - dict2[j])
            
def abs1(dict1,dict2):
    for i in range(1000):
        for j in range(1000):
            abs_value = abs(dict1[i] - dict2[j])

    
"""

setup2 = """
# Generate test data set
from random import randint

dict1 ={}
dict2 = {}
for i in range(1000):
    dict1[i] = randint(0,255)
    dict2[i] = randint(0,255)

# Dictionary lookup
def method2(dict1,dict2):
    # setup lookup dictionary
    lookup_dict = {}
    for i in range(256):
        lookup_dict[i] = {}
        for j in range(256):
            lookup_dict[i][j] = (i-j)**2
    
    # calculate square
    for i in range(1000):
        for j in range(1000):
            distance_squared = lookup_dict[dict1[i]][dict2[j]]
            
def abs2(dict1,dict2):
    for i in range(1000):
        for j in range(1000):
            abs_value = dict1[i]-dict2[j] if dict1[i] >= dict2[j] else dict2[j] - dict1[i]


def abs3(dict1,dict2):
    for i in range(1000):
        for j in range(1000):
            abs_value = ((dict1[i]-dict2[j])**2)**(0.5)

"""

t = timeit.Timer(stmt="method1(dict1,dict2)", setup=setup1)
print(t.timeit(1))

t = timeit.Timer(stmt="method2(dict1,dict2)", setup=setup2)
print(t.timeit(1))


t = timeit.Timer(stmt="abs1(dict1,dict2)", setup=setup1)
print(t.timeit(1))

t = timeit.Timer(stmt="abs2(dict1,dict2)", setup=setup2)
print(t.timeit(1))

t = timeit.Timer(stmt="abs3(dict1,dict2)", setup=setup2)
print(t.timeit(1))



# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import test"))

# pythonic = timeit.timeit('method1(dict1,dict2)', number=1)
# print(pythonic)