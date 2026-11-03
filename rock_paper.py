import random 

print("Welcome to Rock, Paper, Scissors")

choose = int(input("What do you choose? Type 0 for rock, 1 for paper ,2 for scissors: "))
pc_turn = random.randint(0,2)

options = ["rock","paper","scissors"]
print(f"you chose: {options[choose]}")
print(f"Compute chose: {options[pc_turn]}")

if choose == pc_turn:
    print("It's a draw!")
elif(choose == 0 and pc_turn == 2) or (choose == 1 and pc_turn == 0) or (choose == 2 and pc_turn == 1):
    print("You win!")
else:
    print("You lose!")        