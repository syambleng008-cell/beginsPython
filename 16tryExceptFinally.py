print("Error Handling In Python:\n\n")
"""
a = input("Enter a num:\n")
print(f"Multiplication table of {a}:")
try:
    for i in range(1, 11):
        # using int() to convert user input number to integer.

        print(f"{int(a)}X{i}={int(a)*i}")
# except:
# print("Invalid Input.")
except Exception as e:
    print(e)

print("She is Gone.")
print("She really is Gone.")

#handling specific type of error like value error handling
try:
    num=int(input("Enter an integer:\n"))
except ValueError:
    print("Number is not an interger.")
#indexError
try:
    num=int(input("Enter an integer:\n"))
    a=[6,3,9,"John","pkr"] 
    print(a[num])#num is index for a dictionary
except ValueError:
    print("Number is not an interger.")    
except IndexError:
    print("Index Error.")

"""


print("\n\nFinally Clause:")
"""
codes or programs inside finally runs
whether thers occurs error or not.

"""
try:
    l = [1, 90, 7, 8]
    i = int(input("Enter the index:\n"))
    print(l[i])
except:
    print("Some Error Occured.")

finally:
    print(f"I don't give f about Error.")

"""
 finally makes difference in functions.
It will execute even after return.
"""

def func1():
    try:
        l = [1, 90, 7, 8]
        i = int(input("Enter the index:\n"))
        print(l[i])
        return 1
    except:
        print("Some Error Occured.")
        return 0

    # finally:
    # print(f"I don't give f about Error.")


x = func1()#calling function func1()
print(x)





