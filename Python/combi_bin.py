# combination

def comb(n,topick, picked):
    if topick ==0:
        c_list.append(list(c))
    else:
        for i in range(picked,n-topick+1):
            c[topick-1] = A[i]
            comb(n,topick-1,i+1)

A = ['a', 'b', 'c', 'd', 'e']
N = len(A)
r = int(input())
c = [0] * r
c_list = list()
comb(N,r,0)
print(c_list)