t = " welcome to KBC!!\n\n"
print(t.upper())
ques = [
    [
        "Which is the capital of Nepal ?",
        "kathmandu",
        "Pokhara",
        "Dhankuta",
        "Biratnagar",
        1,
    ],
    [
        "Which is the capital of india ?",
        "kathmandu",
        "Pokhara",
        "Delhi",
        "Biratnagar",
        3,
    ],
    [
        "Which is the capital of China ?",
        "kathmandu",
        "Pokhara",
        "Beijing",
        "Biratnagar",
        3,
    ],
    [
        "Which is the capital of England ?",
        "kathmandu",
        "Pokhara",
        "Dhankuta",
        "London",
        4,
    ],
    [
        "Which is the capital of Portugal ?",
        "kathmandu",
        "Pokhara",
        "Lisbon",
        "Biratnagar",
        3,
    ],
    [
        "Which is the capital of Spain ?",
        "kathmandu",
        "Madrid",
        "Dhankuta",
        "Biratnagar",
        2,
    ],
    [
        "Which is the capital of USA ?",
        "kathmandu",
        "Washinton DC",
        "Dhankuta",
        "Biratnagar",
        2,
    ],
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(ques)):
    q = ques[i]  # gonna use 'q' to code inside 'for loop' to iterate list of questions
    print(f"\nQuestion for {levels[i]}:")
    print(f"{q[0]}:")
    print(f"1.{q[1]} 2.{q[2]} 3.{q[3]} 4.{q[4]}")
    user = int(input("Enter your  answer 1-4 or Press 0 to Quit:\n"))
    if user == 0:  # for quitting
        break
    elif user == q[-1]:
        print(f"Correct Answer!! You got Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
    else:  # wrong and invalid input
        print("\n\nWrong Answer.")
        break


print(f"You are taking home Rs.{money}  with you!!")
