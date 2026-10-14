import pandas

# Ways of importing modules and its items:
#from greet import greet as g, s#our own module
import random as r
import math

# import math as m
# import math*# its not recommended. cuz it imports all the function from function and may lead to confusion
# from math import sqrt, pi as p, floor  # using from keyword

print("How import works in Python:")
"""
importing in python is the process of 
loading code from a python module into 
the current script.This allows us to use
functions and variables definfed in the
module in our current script.
"""

print(f"The version of Pandas is:{pandas.__version__}")
print(f"The git version is :{pandas.__git_version__}")
a = math.floor(4.345)
b = math.sqrt(16)
print(f"{a},{b}")
"""
d = m.sqrt(25)  # m is math
print(d)
"""
"""
# using from keyword
a = floor(4.0023456)
b = sqrt(25)
c = a * p  # p is pi from math module
print(f"{a}\nThe sq root of 125 is {int(b):.1f}")
print(f"The value of c is {c:.2f}")#c:.2f prints only two digits after(.)
"""
# dir function: to see all the content of module
print(f"Items in module math are: {dir(math)}\n")
print(f"Items in module Pandas are:{dir(pandas)}")
print(f"Items in module random are:{dir(r)}")
"""
g()
print(s)
"""


# print("Virtual Environment in Python:\n\n")
"""
A virtual environment is an isolated
 folder that has its own Python and
  its own installed packages, separate 
  from the rest of your computer."""
"""  
Simple idea: one project = one virtual
 environment = no package conflicts.
"""
