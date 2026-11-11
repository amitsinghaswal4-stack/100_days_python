#addition of scores
student_score = [89,67,64,34,54,87,87,96,64,34,23,37,98]

sum = 0
for score in student_score:
    sum += score

print(sum)

#negative step
negative_step = range(10,0,-1)
for x in negative_step:
    print(x)

#multiplication table of 7 up to 7 × 10, formatted like 7 x 3 = 21
number = range(1,11)

product = 7
for x in number:
    total = product*x
    print(f"{product} X {x} = {total}")