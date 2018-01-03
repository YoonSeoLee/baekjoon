scale = list(map(int, input().split()))

ascendScale = list(scale)   
descendScale = list(scale)  #list붙이면 되고, 안붙이면 틀림

ascendScale.sort()
descendScale.sort(reverse=True)

if scale == ascendScale:
    print("ascending")
elif scale == descendScale:
    print("descending")
else:
    print("mixed")