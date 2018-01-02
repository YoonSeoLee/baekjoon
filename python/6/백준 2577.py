A = int(input())
B = int(input())
C = int(input())

n = A * B * C

n = str(n)

nList = list(n)
nDic = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

for i in nList:
    if i in nDic:
        nDic[i] += 1

for i in nDic:
    print(nDic[i])
