# combination
# def combi(n,topick, picked):
#     if topick ==0:
#         print(*comb)
#     else:
#         for i in range(picked,n-topick+1):
#             comb[topick-1]= A[i]
#             combi(N,topick-1, i+1)

'''
조합함수 구조  주석
조합 함수 인자(전체개수, 뽑아야하는 수, 뽑은 수)
    만약 뽑아야할 수가 0개라면
        뽑힌애들 프린트
    그게 아니라면,
        뽑을 숫자들 리스트에서 안뽑힌 애들 중에
            조합 남은 자리에 하나 추가
            조합 함수 호출(전체수, 뽑아야할수 -1, i +1)
'''


def combi(n,topick,picked):
    if topick ==0 :
        c_list.append(tuple(comb))
        return
    else:
        for i in range(picked, n-topick +1):
            comb[topick-1] = A[i]
            combi(n,topick-1,i+1)


A = [1, 2, 3, 4, 5]
N = len(A)
r = 3
comb = [0] * r
c_list=list()
combi(N, r, 0)
print(c_list)