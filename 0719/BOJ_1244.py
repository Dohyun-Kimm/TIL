def switch_func(g,loc,s_list):
    if g ==1:
        for a in range(loc-1,len(s_list)): # loc 2 일때  1부터
            if ((a+1) % loc)  ==0 and (a+1)>=loc:
                s_list[a] = (s_list[a]+1)%2
    elif g == 2:
        cursor=1
        s_list[loc -1] = (s_list[loc -1] +1) % 2
        while True:
            if (loc-1 - cursor <= -1 ) or (loc -1 +cursor == len(s_list)):
                break
            # loc 기준으로 대칭에 있는 인덱스 값이 다를때 탈출
            elif s_list[loc-1 - cursor] != s_list[loc -1 +cursor]:
                break
            # 같으면 대칭에 있는 인덱스 값 변화
            elif (s_list[loc - 1-cursor] ==s_list[loc - 1+cursor]):
                s_list[loc - 1-cursor] = (s_list[loc- 1-cursor]+1)%2
                s_list[loc-1+cursor] = (s_list[loc-1+cursor]+1)%2
                cursor +=1
                
            

    return s_list

# 입력
switch_n = int(input()) #스위치 개수
switch_s = input()      #스위치 정보
switch_l = switch_s.split() # 스위치 리스트
for i in range(len(switch_l)):
    switch_l[i] = int(switch_l[i])
student_n = int(input()) #학생수

# 처리
for j in range(student_n):
    input2 = input().split()
    gender = int(input2[0])
    s_loc= int(input2[1])
    switch_func(gender,s_loc,switch_l) # 스위치 변화 처리과정

#출력
output = map(str, switch_l)
if len(switch_l)<20:
    print(' '.join(output))
else:
    for i in range(len(switch_l)//20 +1):
        output = map(str,switch_l[i*20 : (i+1)*20])
        print(' '.join(output))
        