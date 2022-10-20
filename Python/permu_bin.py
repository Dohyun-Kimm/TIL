# permu
def permu(n,topick,picked):
    if picked==topick:
        p_list.append(list(p))
        return
    else:
        for i in range(n):
            if used[i] ==0:
                used[i] = 1
                p[picked] = A[i]
                permu(n,topick, picked +1)
                used[i] = 0


A = ['a', 'b', 'c', 'd', 'e']
N = len(A)
r = int(input())
used =[0]*N
p = [0] * r
p_list = list()
permu(N,r,0)
print(p_list)