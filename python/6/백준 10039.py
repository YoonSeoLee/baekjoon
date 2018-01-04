sum = 0

for i in range(5):
    student = int(input())
    if student < 40:
        student = 40
    sum += student

print(int(sum / 5))