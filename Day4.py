# Rock Paper Scisors
import random

rock = '''
    _______
---'   ____)
       (_____)
      (______)
       (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)                                                                                                                                                      
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

player = int(
    input("Game Time!\n1 - Rock\n2 - Paper\n3 - Scissors\n Choose a number: "))

if player == 1:
    print(f"You chose Rock!\n{rock}")
elif player == 2:
    print(f"You chose Paper!\n{paper}")
elif player == 3:
    print(f"You chose Scissors!\n{scissors}")

pc1 = random.randint(1, 3)

if pc1 == 1:
    print(f"PC chose Rock!\n{rock}")
elif pc1 == 2:
    print(f"PC chose Paper!\n{paper}")
elif pc1 == 3:
    print(f"PC chose Scissors!\n{scissors}")

if player > 3:
    print("You didn't choose a valid option!")
elif player == 1 and pc1 == 3:
    print("You Won!")
elif pc1 == 1 and player == 3:
    print("You Lost!")
elif player > pc1:
    print("You Won!")
elif pc1 > player:
    print("You Lost!")
elif player == pc1:
    print("It's a Draw!")
