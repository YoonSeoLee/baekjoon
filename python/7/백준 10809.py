S = input()
sList = list(S)

alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in alphabetList:
    if i in sList:
        print(sList.index(i), end=' ')
    else:
        print("-1", end=' ')