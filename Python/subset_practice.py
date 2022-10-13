# 부분집합 비트연산자로 만들기

A = list(range(1,6))
print(A)
subset = list()
for i in range( 1,1 << len(A)):
    for j in range(len(A)):
        if i & ( 1 <<j):
            subset.append(j)
    print(subset)