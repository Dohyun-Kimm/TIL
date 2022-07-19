# 남 : switch_n 이 self_n의 배수라면 바꾼다
# 여 :  받은 번호 중심으로 대칭으로 대응되는 
# '스위치 번호'의 '스위치 상태가 같으면
# 스위치를 바꾼다. 

# 스위치 개수 입력 (줄당 최대 20개)
#  스위치 초기 상태 list 형태
# 학생수 100이하
#  남1 여2 / 받은 숫자
# 윗줄 이랑 똑같음.(학생수만큼 반복)


# 스위치를 바꾸는 함수 a= (a+1)%2

"""
ex = [0,1,0,1,0,0,0,1]

function(성별, 숫자):
    if 성별 ==1:
        for i in range(1,len('스위치 리스트')): #1부터 시작 해서 1뺀 인덱스에 반영
            if i % 숫자 == 0 :
                '스위치 리스트'[i-1] = (i+1)%2

    elif 성별 == 2:
        cursor=0
        
        while True:
            cursor += 1
            if (숫자-1 +cursor == len(스위치 리스트)) or (숫자 - 1-cursor ==0):
                break
            elif (스위치 리스트[숫자-1 -cursor] == 스위치 리스트[숫자-1 +cursor]):
                스위치 리스트[숫자-1 -cursor] = (스위치 리스트[숫자-1 -cursor]+1) %2
                스위치 리스트[숫자-1 +cursor] = (스위치 리스트[숫자-1 +cursor]+1) %2
        
"""

def switch_func(g,loc,s_list):
    if g ==1:
        for a in range(loc-1,len(s_list)): # loc 2 일때  1부터
            if ((a+1) % loc)  ==0 and (a+1)>=loc:
                #print('here')
                s_list[a] = (s_list[a]+1)%2
                #print('after s1',s_list)
    elif g == 2:
        cursor=1
        s_list[loc -1] = (s_list[loc -1] +1) % 2
        #print('length', len(s_list))
        while True:
            #print('index now',s_list[loc-1-cursor])
            if (loc-1 - cursor <= -1 ) or (loc -1 +cursor == len(s_list)):
                break
            # loc 기준으로 대칭에 있는 인덱스 값이 다를때 탈출
            elif s_list[loc-1 - cursor] != s_list[loc -1 +cursor]:
                break
            # 같으면 대칭에 있는 인덱스 값 변화
            elif (s_list[loc - 1-cursor] ==s_list[loc - 1+cursor]):
                # loc=3, 
                s_list[loc - 1-cursor] = (s_list[loc- 1-cursor]+1)%2
                s_list[loc-1+cursor] = (s_list[loc-1+cursor]+1)%2
                cursor +=1
                #print('after s2',s_list)
            

    return s_list


switch_n = int(input())
switch_s = input()
switch_l = switch_s.split()
for i in range(len(switch_l)):
    switch_l[i] = int(switch_l[i])
student_n = int(input())

for j in range(student_n):
    input2 = input().split()
    gender = int(input2[0])
    s_loc= int(input2[1])
    switch_func(gender,s_loc,switch_l)

    
for i in range(len(switch_l)):
    print(switch_l[i],end=' ')
    