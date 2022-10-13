# 조합 함수 만들기
def nCr(n,r,s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1,i+1)

# 부분 집합의 합 구하기

'''
 정수 10개의 정수집합에 대한 모든 부분 집합중 합이 0이되는 부분집합 구하기

'''

A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# A = [1,2,3,4,5]
N = len(A)
cnt = 0
# for i in range(1<< N):
#     subset= list()
#     for j in range(N):
#         if i &(1<<j):
#             subset.append(A[j])
#             # print(A[j],end=' ')
#     if sum(subset)==0:
#         cnt +=1
# print(cnt)
r = 3
comb = [0]*r
nCr(N,r,0)
