print("tuple:")
"""
Very similar to lists but not changeable.
separated by coma enclosed by ().
used when constant lis is required while 
developing program.
"""

tup = (1, 4, 7, 8, 9, 10, "Seiso", True)
tp = (1,)  # if single element must be coma after it
# tp=(1)#returns type int cuz single element and bo coma
print(type(tp), tp)
print(type(tup), tup)
print(len(tup), tup)
print(tup[0])
print(tup[:])  # in bg print(tup[0:len(tup)])
print(tup[1])
print(tup[3])
print(tup[4])
print(tup[6])
print(tup[-3])  # print(tup[len(tup)-3]) is how it executes in bg


if 300 in tup:
    print("Yes")
else:
    print("No")

# slicing
tup2 = tup[2:6]
print(tup2)






