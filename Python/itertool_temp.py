# subset

A = [1,2,3,4,5]
N = len(A)
subset = []
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 <<j):
            print(A[j],end=' ')
            subset.append(A[j])
    print(subset)