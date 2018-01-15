#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ex 4-3
for value in range(1,21):
    print(value)
#4-4
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
#4-5
print(sum(numbers))
#4-6
even_numbers = list(range(1,21,2))
print(even_numbers)

ex_numbers = []
for value in range(1,21,2):
    ex_numbers.append(value)
    print(ex_numbers)
#4-7
list = list(range(3,31,3))

list = []
for value in range(3,31):
    list.append(value*3)
print(list)
#4-8
cube = []
for value in range(1,11):
    cube.append(value**3)
print(cube)
#4-9
cube = [value**3 for value in range(1,11)]
print(cube)
