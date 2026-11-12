#password genration
import random

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
           ,'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','/',]

nr_letters = int(input("How many letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#easy level
password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0,nr_symbols):
    password += random.choice(symbols)

for char in range(0,nr_numbers):
    password += random.choice(numbers)

print(f"Easy password: {password}")    

chars = list(password)
random.shuffle(chars)
result = "".join(chars)
print(f"Hard password {result}")
