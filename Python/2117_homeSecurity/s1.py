# 홈 방범 서비스
'''
문제 요약
 도시의 크기 :N*N
 서비스 범위 : 중심점으로부터 거리가 k인 영역 (가로세로합 k)
 운영 비용: K^2 + (K-1)^2
 집당 지불 할 수 있는 비용 : M
 손해를 보지 않으면서 가장 많은 집에 제공할수있는 서비스 영역을 찾고,
 서비스 받는 집의 수를 구하기.

 서비스 영역*M < K^2 + (K-1)^2 이면 계산 하지 않기.
 집의 수 * M > K^2 + (K-1)^2 일떄 집의 수 구하기.
'''

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    area = []* N
    for _ in range(N):
        area.append(list(map(int,input().split())))
        # print(area)
#  k의 최대 값은 N//2 +1

    for i in range(N):
        for j in range(N):
            pass

'''
교수님 풀이
    집이 있는 곳의 좌표를 튜플로 받아서 리스트에 저장
    방범 서비스를 제공하는최대 범위를 기준으로, k를 하나씩 줄여 가면서 계산시작
        K 일때 가능한 이익 계산.
        범위 안에 들어있는 집의 수 계산.
        이익이 0이상이면서. 집의 수가 이전 최대 집의 수보다 크다면 갱신
'''