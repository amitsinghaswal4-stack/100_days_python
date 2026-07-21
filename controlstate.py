num_1 = float(input("enter first number: "))
num_2 = float(input("enter second number "))

operation = input("choose your operation + , - ,*")

if operation == "+":
    print(f"Addition of both number is {num_1 + num_2}")

elif operation == "-":
    print(f"Differnce of both number is {num_1 - num_2}")

elif operation == "*":
    print(f"Product of both number is {num_1 * num_2}")

else:
    print("invalid choice")