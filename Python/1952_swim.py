# 1952 수영장
'''
DP를 이용해서 풀어보기
1. 1일치, 1달치 비교해서 최저가 로 DP 채우기
2. 3달치 비교해서 DP 업데이트
3. 1년 짜리와 비교하기
'''

T= int(input())
for tc in range(1,T+1):
    # 가격표 입력 받기
    day, month, month_3, year = map(int, input().split())
    # 이용 계획
    plan = list(map(int,input().split()))
    # dp표 만들기
    dp = [0] * 12
    # 1일 권 총합, 1달권 총합
    for i in range(12):
        dp[i] = min(day*plan[i]+dp[i-1], month+dp[i-1])
        # 3달권 비교 3 달 마다 비교 하는 것이 아니라, 3달권을 쓸 수 있을때부터 비교
        if i >= 2:
            dp[i] = min(dp[i-1]+day*plan[i] , month+dp[i-1],month_3+dp[i-3])
    # 1년권 비교
    ans = min(dp[-1],year)
    print('#{} {}'.format(tc,ans))
