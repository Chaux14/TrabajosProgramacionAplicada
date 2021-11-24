A=[5,3,4,2]
B=[1,4,7,9]

n=len(A)//2
x=[((A[i+1])**2*B[2*i])+B[n+i] for i in range(n)]
print(x)