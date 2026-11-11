import random

print("Welcome to Rock paper and scissors")

choose = int(input("What is your choic? 0 for Rock, 1 for paper, 2 scissor:  "))
pc_turn = random.randint(0,2)

options = ["rock","paper","scissors"]
print(f"your choice is {options[choose]}")
print(f"computer choice is {options[pc_turn]}")

if choose == pc_turn:
    print("it is a draw")
elif(choose == 0 and pc_turn == 2) or (choose == 1 and pc_turn == 2 ) or (choose == 2 and pc_turn == 1):
    print("you win")
else:
    print("you lose")  