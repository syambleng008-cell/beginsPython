print("match case statements:")
# new edition of python3.10 same as switch case as in other compiler
"""number = int(input("Enter an interger:\n"))
match number:
    case 1 | 2 | 3:
        print("Small number")
    case 4 | 5 | 6:
        print("Medium number")
    case _:
        if number > 20:
            print("Very big number")
        elif number > 10:
            print("Big number")
        else:
            print("Number is 0 or negative or between 7 and 10")
"""

print("\nloopings in Python:")
print("for loop:")
nm = "Araspaj"
for i in nm:
    print(i)
    if i == "p":
        print("This is P.Wowo!")
fr = ["apple", "banana", "orange"]
for f in fr:
    print(f)
    for i in f:
        print(i)
print("range():")
for k in range(30):
    print(k + 1)
for k in range(1, 15):
    print(k)
for k in range(1, 12, 2):  # range(start, stop, step)

    print(k)
#indexing starts with 0 in programming languages.    


print("\nwhile loop:")    
"""Executes only if the condition is True.
idealy we use while with complex conditions."""    
i=0
while(i<3):
    print(i)
    i=i+1
print("\n")    
#Decrementing while loop.
i=5
while(i>0):
    print(i)
    i=i-1
else:
    print("condition became false in while loop.")    
    
print("\nEmulating do…while loop in python")
i = 0
while True:#infinite loop cuz the condition is true
    print(i)
    i = i + 1
    if i % 10 == 0:
        break

    
print("\nbreak and continue statements:")
# breaks :end the whole loop wheras continue
# just skips the given iteration

print("\nbreak:")
for i in range(12):
    if i == 10:
        print("exited loop.")
        break
    print("5 X", i, "=", 5 * i)

print("\nconinue:")
for i in range(12):
    if i == 10:
        print("Skipped the Iteration")
        continue
    print("5 X", i, "=", 5 * i)







