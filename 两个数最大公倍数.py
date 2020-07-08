def minerr(A, B):
    if A==0:
        return 0
    if A > B:
        result = A - B
        return minerr(B, result)
    elif A < B:
        result = B - A
        return minerr(A, result)
    else:
        return A

n = input().split()
A = int(n[0])
B = int(n[1])
result = A * B / minerr(A,B)
print(int(result))




