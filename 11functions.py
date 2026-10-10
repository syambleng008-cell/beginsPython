print("Functions:\n")
""" they are used to save time and lake programming 
easy. instead of typing repated code again and
and again we create an entity known a  function
two Types:
    Builtin functions:sum(),range(),set(),
                      print(),len() etc.
    User defined fucntions: Defined by user
    using def keyword.  
    syntax; def funcName(parameters):
"""

def calcgmean(a, b):  # creating function
    mean = (a * b) / (a + b)
    print("The geometric mean is ", mean)

def isGreater(a,b):
    if a > b:
        print("First number is greater.")
    else:
        print("Sec number is greater or Equal.")
 
def isLesser(a,b):
    pass#to write code later or when needed.
  
a = 9
b = 8
isGreater(a,b)
"""if a > b:
    print("First number is greater.")
else:
    print("Sec number is greater or Equal.") 
    """
# gmean=(a*b)/(a+b)
# print("The geometric mean is ",gmean)
calcgmean(a, b)  # Using function
c = 10
d = 12
isGreater(c,d)
calcgmean(c, d)  # Using function

print("\n\nFunction Arguments:")
def average(*num):
    print(type(num))
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)
    return 88#first return is returned.

c= average(1,2,7,8,10)
print(c)


def nm(**name):
    print(type(name))
    print("Hello",name["fname"],name["Mname"],name["Lname"])

nm(Mname="Bdr",Lname="Magar",fname="Phool")#callinh nm function

