print("String slicing[]:")
names = "Ram,hari,rita,guta,sita"
print(names[4:8])
print(len(names))  # use len()to find the lenth of strind
# for slicing we use []
print(names[0:5])
# python'special feature
print(names[:5])
print(names[:])
print("negative slicing")
print(names[0:-8])  # python automatically puts len()function before-number
print(names[-1:-8])  # does not make sense
print(names[-8:-1])
nm = "harry"
print(nm[-4:-2])
print("\n")
print("String Methods:")
print("\'String methods operates on existing\noperator and creates new string\'")
#Strings are immutuable rather new strind is created
a="seiso"
print(len(a))
print(a.upper())
print(a.lower())
print("strip() method:")
b="!!wow!!!!"
print(b)
print(b.rstrip("!"))
print("\n")
print("replace() method:")
n="seisoseisoDon"
print(n)
print(a.replace("seiso","Tou"))
print("\n")
print("Split():")
print("\'Converts strings to lists.\'")
nn="!!wowoowow so dangerousboy wowoowoiw!!!"
print(nn)
print(nn.split(" "))
print("\n")
print("capitalize():")
#it only capitalises the first character
blog="welCome tO My profile"
print(blog.capitalize())
print("cente():")
str2="Welcome to the stream!"
print(str2)
print(len(str2))
print(str2.center(50))
print(len(str2.center(50)))
print("\n")
print("count():")#coubts how many times is repeated
print(str2.count("e"))
print("\n")
print("endswith():")
print("Returns boolians datatypes.")
print(str2.endswith("!"))
print(str2.endswith("!?"))
str= "we are good guys"
print(str.endswith("e",1,6))
print("\n")
print("find():")
#find() tzkes first occurence of a charater or element
a="he is a good boy ,your son."
print("The first index if y is:",a.find("y"))






