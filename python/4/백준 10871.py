N, X = map(int, input().split())

A = list(map(int, input().split()))
smallList = []


for i in A:
    if i < X:
        smallList.append(i)

for j in smallList:
    print(j, end=' ')
