print("String foramtting in python:\n")
# og method: no problem but not convenient
letter = "I am {0} and I am from {1}."
country = "Japan"
name = "Seiso"
print(letter.format(name, country))
# new method: we use f"".
print(f"I am {name} and I am from {country}.")
print(f"I am {{name}} and I am from {{country}}.")
print(f"{2*30:.2f}")
print(type(f"{2*30:.2f}"))


# DocStrings in python:used right after the def of func ,methods,class or modules.
def squar(n):
    """takes a number and returns square
    of the number.#this is doc strings"""
    sq = print(n**2)
    return sq


squar(5)
# prints doc strings in the func using__doc__
print(squar.__doc__)

# print("PEP 8:")
# PEP:Python Enhancement Proposal
# the Zen of Python by Tim Peters is a Poem
# we can access poem by typing import this in console







