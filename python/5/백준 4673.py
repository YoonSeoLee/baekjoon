num = [i for i in range(1, 10001)]

def d(n):
    tmp = list(str(n))
    tmp.append(str(n))
    selfNumber = 0
    for i in tmp:
        selfNumber += int(i)
    return selfNumber

notSelfNumber = []

for i in num:
    if d(i) not in notSelfNumber:
        notSelfNumber.append(d(i))

for i in notSelfNumber:
    if i in num:
        num.remove(i)

for i in num:
    print(i)
