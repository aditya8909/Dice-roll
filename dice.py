import random
want="y"
while want=="y":
    no=random.randint(1,6)
    if no==1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")
        want="n"
        want=input("want to roll again?")
    elif no==2:
        print("-----")
        print("0    ")
        print("     ")
        print("    0")
        print("-----")
        want="n"
        want=input("want to roll again?")
    elif no==3:
        print("-----")
        print("0    ")
        print("  0  ")
        print("    0")
        print("-----")
        want="n"
        want=input("want to roll again?")
    elif no==4:
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")
        want="n"
        want=input("want to roll again?")
    elif no==5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")
        want="n"
        want=input("want to roll again?")
    elif no==6:
        print("-----")
        print(" 0 0  ")
        print(" 0 0 ")
        print(" 0 0 ")
        print("-----")
        want="n"
        want=input("want to roll again?")