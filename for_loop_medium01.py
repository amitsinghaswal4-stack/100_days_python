#program to calculate sum of no.from 1 to 10
total = 0
for i in range(1, 11):
  total += i
print(f'sum is : {total}')
print()

#reverse a word
word = 'python'
for i in range(len(word) - 1,-1,-1):
    print(word[i] , end=" ")
print()

#count vowels in a string
vowels = 'aeiou'
word = 'education'
count = 0

for char in word:
    if char in vowels:
        count+=1

print(f"no of vowel in {word} is : {count}")
