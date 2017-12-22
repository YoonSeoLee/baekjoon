A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

# A > B > C
if A <= B:
    if B <= C:
        print(B)
    elif A <= C:
        print(C)
    else:
        print(A)
elif B <= A:
    if A <= C:
        print(A)
    elif B <= C:
        print(C)
    else:
        print(B)
