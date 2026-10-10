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
print("\n")
print("Index():")
#it is similar to find() but it raises exception
print("isalnum():")
str="Myfavnumberis08"
str1="My fav number is 08!"
print(str.isalnum())#true
print(str1.isalnum())#false
'''isalnum():It returns true only if 
entire string consist of alphanumeric .
Returns false if there is any special
 characters or spaces'''
print("\n")
print("isalpha():")
#returns true if A-Z,a-z else false
s="wow00"
print(s.isalpha())#false
print("islower():")
#a-z
print("isprintable():")
'''returns true if all values given in 
strings are printable'''
st="we are good008"#true
st1="we are good\n"#false
print(st.isprintable())
print(st1.isprintable())
print("\n")
print("isspace():")
'''returns true if strings only and 
only white spaces'''
print("istitle():")
''' returns true only is all the first
 letters of the strings ar capitalised'''
st="We Are Young Boys Club"
st2="We are Young Boys club"
print(st.istitle())#true
print(st2.istitle())#false
print("startswith():")
'''checks the given strings starts
 with which character '''
print("swapcase():")
'''converts Capital letters to small
and vice-versa'''
print("title():")
'''converts string to titles'''
s="my country nepal"
print(s.title())










