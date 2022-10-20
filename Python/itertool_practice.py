# 순열
# def permu(i,k,r):
#     if i ==r:                       # 순열이 다 채워지면
#         print(p)                    # 순열 출력
#     else:
#         for j in range(k):          #
#             if used[j] ==0:         # a[j]가 아직 사용되지 않았다면,
#                 used[j] = 1         # a[j] 사용됨으로 표시
#                 p[i] = a[j]         # p[i]는 a[j]로 결정
#                 permu(i+1,k,r)        # p[i+1] 값 결정하러 재귀
#                 used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제
#                 # 베이비 진 풀어보기
#
# # 반복 있는 순열

# 조합
def nCr(n, r, s):
    if r ==0 :
        print(*comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)
# 반복 있는 조합


# N = 5                               # 10개중
# R = 3                               # 3개 고르기
# a = [i for i in range(1, N+1)]      # 주어진 숫자들
# used = [0] * N                      # 조합 사용 여부 체크하는 리스트
# p = [0] * R                         # 조합 채우는 리스트
# permu(0,N,R)

A = [1, 2, 3, 4, 5]
n = len(A)
r = 3
comb= [0] * r
nCr(n, r, 0)