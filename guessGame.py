# importing random module
import random

tl = "Guess the lucky number Game"
print(tl.title())
# Generating lucky number
lucky_num = random.randint(1, 50)  # genrating random interger between 1-50


# Developing Game concept using function
def guess_num():
    while True:  # infinite loop
        user = int(input("Guess the number:\n"))
        if user == lucky_num:
            print(user, "was the number.You won the Game.")
            break  # to end the loop
        elif user < lucky_num:
            print("Too low.\n")
        else:
            print("Too high\n")
    print("\n\nGame Over!!.Thank you for Playing.")


guess_num()  # calling the gaming function
