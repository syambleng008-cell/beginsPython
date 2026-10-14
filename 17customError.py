print("Raise Cutsom Error in Python:")
"""
Thesee are important while extracting
data from server.
Raising custom errors matters because they:

1. **Make problems clear.** `InvalidAgeError: age cannot be negative` is easier to understand than a generic `ValueError`.
2. **Let you catch specific problems.** You can handle your own errors separately from built-in ones.
3. **Enforce rules.** They stop bad data early, before it causes bigger bugs.

```python
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age

try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)  # Age cannot be negative
"""

a = int(input("Enter any value between 5 & 9:\n"))
if a < 5 or a > 9:
    raise valueError("Invalid Input.")
else:
    print(f"Your number is {a}.")


# Defining custom exceptions using class
class InvalidAgeError(Exception):
    pass


def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    return age


try:
    set_age(-5)
except InvalidAgeError as e:
    print(e)  # Age cannot be negative



#Quick quiz by CodeWithHarry
a = int(input("Enter any value between 5 & 9:\n"))
if a < 5 or a > 9:
    raise valueError("Invalid Input.")
        
elif a=="quit":
    print("fine")
    




