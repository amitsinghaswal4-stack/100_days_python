#print fibonicaa series till 10

a = 0 
b = 1
print(a,b,end= " ")

for _ in range(10):
    next_term = a + b
    a,b = b,next_term
    print(next_term,end=" ")
    
print()
#Calculate factorial of given number
n = 5
factorial = 1

for i in range(1,n+1):
    factorial *= i

print(f"factorial of {n} is {factorial}")
    