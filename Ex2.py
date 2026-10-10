"""
1.capable of showing qsns to the user
2.use list type to store qsns and theri
correct answers
3.Display the final amount the user is taking
after playing the game.
"""

t = "Welcome to the Who will be the millionaire!!"
print(t.title())
u = str(input("Are you ready?\n"))  # asking if they are ready or no
usr = u.lower().strip()  # user can enter any letter

if usr == "yes":
    print("Let's go!!\n")

    # Qsn to ask
    qsn = [
        "which is the capital of Nepal?",
        "when was Messi born?",
        "When was the first football WC stated?",
        "when did WW1 stared?",
        "Where is ronaldo from?",
    ]

    # Answers of the qsns.
    ans = ["Kathmandu", "1987", "1930", "1914", "Portugal"]
    # need to covert everything to lower in qsn and ans
    # checking if they are printable
    """print(qsn,ans)
    print(len(qsn))
    print(len(ans))
    """

    # iterating questions to ask  using range(len()) in for loop
    amount = 0
    for i in range(len(qsn)):
        print(qsn[i])
        u = input()  # taking answer from use

        # for prize amount
        if (
            u.lower().strip() == ans[i].lower()
        ):  # we have already defined i in for loop using range(len())
            if amount == 0:
                amount = 1000
                print("You got", amount, "Congratulation!!\n")
            else:
                amount = amount * 2
                print("You got", amount, "Congratulations!!\n")
        else:
            print("Wrong Answer.\n")
            print(
                "Don't worry you still have chances left.",
            )

        """code to Avoid asking the qsn
         ready for next qsn ir not. if i is
         smaller condition will padd else it
         won't
         """
        if i < len(qsn) - 1:
            s = input("\nAre you ready for next Question?\n").lower().strip()
            if s != "yes":
                break

    # informing user the amount they are taking hole
    print("\nYou are Taking ", amount, "Home!")
    print("\n\nThank You. You are always welcome to Play.")


elif usr == "no":
    print("\n\nThank You. You are always welcome to Play.")
