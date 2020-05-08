#!/usr/bin/env python3
import timeit
from random import randint

# Generate test data set
dict1 ={}
dict2 = {}
for i in range(1000):
    dict1[i] = randint(0,255)
    dict2[i] = randint(0,255)

# Square difference
def method1():
    for i in range(1000):
        for j in range(1000):
            distance_squared = (dict1[i] - dict2[j])    
    
# Dictionary lookup
def method2():
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
            
