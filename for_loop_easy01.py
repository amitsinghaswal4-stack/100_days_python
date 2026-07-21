#print no. from 1 to 5 in a sequence
for i in range(1, 6):
     print(i, end=" ")
print()

#print squares of no. from 1 to 5
for i in range(1, 6):
     x = i**2
     print(x, end=" ")
print()

#print even no. from 1 to 10
for i in range(1, 11):
     if i % 2 == 0:
          print(i, end=" ")
print()

#another method it prints true and false as comparison operatin
for i in range(1, 11):
     x = i % 2 == 0
     print(x, end=" ")
