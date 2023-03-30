print("Hi, what is your name?")

name = str(input())
print("Hello, " + name)

print("You have come to the right place, I will help you set up an investment portfolio. \nHow old are you? It depends on your investment risk.")

age = int(input())
if age < 18:
    print("100% in X!")

# wiek pomiędzy 18, a 30
elif age > 18 and age <= 30:
    print("It's perfect age to start investing! \nHow much money you want to invest?")
    money = int(input())
    if money < 1000:
        print("Invest in X and save some extra money! See you later.")
    elif money > 1000 and money <= 10000:
        print(
            "Spend 50% in X and the rest in Y. "
            "\nHere is my proposal for you: "
            "\n15% X,"
            "\n15% Y,"
            "\n20% Z."
            "\nFor the value stocks search in INDEX X and INDEX Y. Feel free to contact me, we will choose the perspective ones.")
    elif money > 10000 and money <= 100000:
        print(
            "Spend 50% in X and the rest in Y. "
            "\nHere is my proposal for you: "
            "\n20% X,"
            "\n20% Y,"
            "\n10% Z."
            "\nFor the value stocks search in INDEX X and INDEX Y.")
    elif money > 100000:
        print("That's a lot of money! Send me an email, we will figure it out!")

# wiek pomiędzy 30, a 65
elif age > 30 and age <= 60:
    print("It's never late to start an investing career \nHow much money you want to invest?")
    money = int(input())
    if money < 1000:
        print("Oh, come on, risk more!")
    elif money > 1000 and money <= 10000:
        print(
            "Spend 50% in X and the rest in Y. "
            "\nHere is my proposal for you: "
            "\n20% X,"
            "\n20% Y,"
            "\n10% Z."
            "\nFor the value stocks search in INDEX X and INDEX Y. Feel free to contact me, we will choose the perspective ones.")
    elif money > 10000 and money <= 100000:
        print(
            "Spend 50% in X and the rest in Y. "
            "\nHere is my proposal for you: "
            "\n20% X,"
            "\n20% Y,"
            "\n10% Z."
            "\nFor the value stocks search in INDEX X and INDEX Y.")
    elif money > 100000:
        print("That is a lot of money! Send me an email, we will figure it out!")

