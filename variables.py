#!/usr/bin/env python3

"""
Module to learn more about variables in python
"""

floatvar = 3.14
myvar = 12
complexvar = 3j
boolVar = False

print(myvar)
print(f"{myvar} is of type:", type(myvar).__name__)

print(str(myvar) + "is of type" + str(type(myvar)))

print(floatvar)
print(type(floatvar))
print(type(floatvar).__name__)


print(complexvar)
print(type(complexvar).__name__)
print("{} is of the datatype {}".format(complexvar, type(complexvar)))

print(boolVar)
print(type(boolVar))
print("{} is of the datatype {}".format(boolVar, type(boolVar)))