A, B = map(int, input().split())

print(A * B)


# A > B > C
if A <= B:
    if B <= C:
        A, C = C, A
    elif A <= C:
        A, B = B, A
elif A <= C:
    if B <= C:
        print(A)



print(B)
