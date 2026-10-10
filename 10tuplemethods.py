print("Tuples methods:")
"""
we can not change tuple in a direct way.
we must copy it and make new list and 
make changes in the list and then change 
the list to tuple. 
"""
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")      # add item
temp.pop(3)                # remove item
temp[2] = "Finland"        # change item
countries = tuple(temp)
print(countries)

#merging
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count()
tup=(3,14,42,3,5,6,9,10,3,3)
print(len(tup))
#res=tup.count(3)
#print("There are ",res, "threes.")

#index():returns   index of first occurence of the given element
#res=tup.index(3)
res=tup.index(9,2,9,)#(element,first index,end index)searching between desired indexes
#raises value error if there is no entered value in the tuple
print(res)















