# 14888 연산자 끼워넣기
from itertools import permutations, combinations

def calcul(a,b, o):
    if o ==0:
        return a+b
    elif o ==1:
        return a-b
    elif o == 2:
        return a*b
    else:
        return a//b

def dfs(idx, ops, r):
    global ans_max, ans_min
    # print(r)
    # print(ops)
    if idx == N:
        print(r)
        ans_max = max(ans_max,r)
        ans_min = min(ans_min,r)
        return
    for i in range(4):
        if ops[i]:
            opp = ops[::]
            opp[i] -= 1

            # r =calcul(r,nums[idx],ops[i])
            # print(f'{r=} {ops[i]=}')
            print(f'brefore calcul:{r=}')
            r =calcul(r,nums[idx],i )
            print(f'{opp=} {r=}')
            dfs(idx+1,opp,r )
    print()


N = int(input())
nums = list(map(int, input().split()))
operands = list(map(int, input().split()))
result = nums[0]
ops = operands[::]
ans_max = -float('inf')
ans_min = float('inf')
#  연산자 인덱스, 수열 인덱스, 결과 값,
#  각 연사자들로 부터 시작해서 수열 채우기
dfs(1,ops,result)


print(ans_max)
print(ans_min)

