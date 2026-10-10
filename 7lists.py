print("Lists:")
"""
store multiple values in single variable
items are separated by comas and are enclose
within [].They are changeable.

"""
v=[2,3,5,"Seiso",True,5,7,9,90]
print(type(v))
print(v[0])
print(v[1])
print(v[2])
print(v[3])
print(v[4])
print(v)
print(v[:])
print(v[1:6])
print(v[1:8:2])
print("The length of V is ",len(v))
"""to convert neg indexing into positive
we use len()-neg index."""
if 8 in v:#we use 'in' keyword to find if the element is in the list or not
    print("Yes")
else:
    print("No")    
#same thibgs apply for strings
"""if "eau" in "Beautiful":
    print("Yes")
else:
    print("No")    
"""    
print("\n lisr comprehension:")
"""

"""
lst=[i*i for i in range(8)]
print(lst)

lst=[i*i for i in range(8) if i%2==0]
print(lst)
    








    
    
   
   
   
   
   




    


