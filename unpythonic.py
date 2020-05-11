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
    dict1[i] = randint(1,16)
    dict2[i] = randint(1,16)

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


def get_manhattan(current, goal):
    distance_x = (goal-1)%4 - (current-1)%4
    # distance_y = (goal-1)//4 - (current-1)//4
    d_man_x = 1 if distance_x == 3 or distance_x == -3 else distance_x if distance_x >= 0 else distance_x*-1
    # d_man_y = 1 if distance_y == 3 or distance_y == -3 else distance_y if distance_y >= 0 else distance_y*-1
    # return (d_man_x**(0.91) + d_man_y**(0.91))**(1.414)
    return d_man_x
    
def abs4(dict1,dict2):
    for i in range(1000):
        for j in range(1000):
            abs_value = get_manhattan(dict1[i],dict2[j])
    
    
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

t = timeit.Timer(stmt="abs4(dict1,dict2)", setup=setup2)
print(t.timeit(1))



# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import test"))

# pythonic = timeit.timeit('method1(dict1,dict2)', number=1)
# print(pythonic)