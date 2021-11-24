A = [4, 3, 1]
B = [2, 1, 4]
C = [0, 1, 0]

n = len(A)

x = sum((A[i] * B[i]) + C[i] for i in range(n)) + n * n

print(x)
