"""
age = int(input("enter your age: "))
if age >= 18:
  print("you are eligible to vote")
else:
  print("you are not eligible to vote")
  """
age = int  (input("enter your age: "))
if age <= 18:
   print(f"you are {age} years old and you are child")
elif age<25:
   print(f"you are {age} years old and you are young")
elif age<50:
   print(f"you are {age} years old and you are adult")
else:
   print(f"you are {age} years old and you are old")