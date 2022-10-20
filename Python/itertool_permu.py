# 순열
A = [1,3,5,7,9]
N = len(A)
C = 3
p = [0]*C
p_list=list()
used = [0] * N

#
# def permu(n, topick, picked):
#     if picked == topick:
#         return print(p)
#     else:
#         for i in range(n):
#             if used[i] ==0:
#                 used[i] =1
#                 p[picked] = A[i]
#                 permu(n,topick,picked+1)
#                 used[i] = 0

'''
순열 주석 스켈레톤
함수(전체 개수,뽑아야하는수, 뽑힌 수들)
    만약 뽑아야하는수랑 뽑힌 수랑 같으면
        함수 종료 하고 조합 리턴 받기
    
    그게 아니라면
        전체 숫자들을 하나씩 보면서
            그 숫자가 이미 사용된 숫자가 아니라면
                사용한다는표시를  하고
                순열에 추가하기
                다음 숫자 뽑기위해 함수 호출(전체숫자, 뽑아야하는 숫자, 뽑힌 수 +1)
                사용한거 제자리해놓기            
'''

def permu(n,topick,picked):
    if picked == topick:
        print(p)
        p_list.append(tuple(p))
        return

    else:
        for i in range(N):
            if used[i] == 0:
                used[i] =1
                p[picked] = A[i]
                permu(n,topick, picked+1)
                used[i] = 0


permu(N,C,0)
print(p_list)