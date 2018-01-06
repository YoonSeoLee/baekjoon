N = int(input())

numList = []

for i in range(N):
    n = int(input())
    numList.append(n)

numList.sort()

for j in numList:
    print(j)