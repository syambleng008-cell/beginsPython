print("Dictioneries{} in Python:\n")
"""
are ordered of data items.key-value 
pairs .They store multiple items in a
single variable.
"""

student = {"name": "Ram", "age": 20, "city": "Pokhara"}

print(student["name"])  # Ram
print(student.get("name"))  # if there is no key it does not return error
student["age"] = 21  # change a value
student["grade"] = "A"  # add a new key
print(student.keys)
print(student.values)
print(student)  # {'name': 'Ram', 'age': 21, 'city': 'Pokhara', 'grade': 'A'}
# Using loops to print
for i in student.keys():  # getting all the keys
    print(student[i])

# getting all the values
for i in student.keys():
    print(f"The value coresponding to the key {i} is {student[i]}")
print("\n")
print(student.items())  # prints key-vlalue pairs
for i, f in student.items():  # where i is key and f is value
    print(f"The value coresponding to the key {i} is {f}")

print("\nDictionary Methods:")
ep1={12:45,31:89,567:80,88:98}    
ep2={87:98,34:67}
print(ep1)
print(ep2)

#update():
#ep1.update(ep2)
#print(ep1)

#clear()
#ep2.clear()#clears the dictionary
#print(ep2)#empty dictionary
#empty dictionary syntax dictname={}

#pop():removes a random key-value pair
#ep1.pop(567)
print(ep1)    
#popitem():removes last's key-value pair
ep1.popitem()
print(ep1)

#del keyword:deletes a whole dictionary
col={"Red":2,"Green":5,"Blue":6}
del col["Red"]#deletes red key value pair
print(col)
del col#deletes the col dictionary
#print(col)#throws error












