import random
print(" 0 - Tails, 1 - Heads")
p1 = int(input("Head or tails? "))
if p1 == 1:
    print("You chose Heads!")
else:
    print("You chose Tails!")

head_tails = random.randint(0, 1)
if head_tails == 1:
    print("> Heads")
    if p1 == 1:
        print("You won!")
    else:
        print("You lost!")
else:
    print("> Tails")
    if p1 == 0:
        print("You won!")
    else:
        print("You lost!")
