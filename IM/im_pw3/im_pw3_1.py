# 첫 10개만 보여주면됨
# 연산의 위치가 10이하인 명령어만 처리하면 됨
# append 갖다버리기
def length(q):
    count = 0
    for _ in q:
        count += 1
    return count


# I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.
def insert(x, y, s):  # x: index, y: numbers, s: list
    global line
    temp =  [] * 4000
    for a in range(N-1):
        if a == int(x):
            for b in range(y):
                temp.append(s[b])
        # print(a, end=' ')

        temp.append(line[a])

    return temp


# D(삭제) x, y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제

for t in range(10):
    N = int(input())
    line = input().split()

    M = int(input())
    commands = input().split()
    # M읜 명령어의 개수 , command  =  명렁어 수, 파라메터 포함 길이
    # print(M, len(commands))
    command_menu = ['A', 'I', 'D']
    flag = 0
    while flag < length(commands):
        # print(flag)
        if commands[flag] in command_menu:
            if commands[flag] == 'I':
                flag += 1
                # 제거위치
                if int(commands[flag]) < 10:  # command I 이면서 삽입 위치가 10 이하면 함수 시행
                    # print('I location:', commands[flag])
                    command_index = commands[flag]
                    flag += 1
                    insert_list = list()
                    command_numbers = int(commands[flag])  # 몇번 시행할지
                    # 제거 횟수
                    for _ in range(command_numbers):  # 시행 횟수만큼 리스트에 추가
                        flag += 1
                        insert_list.append(commands[flag])
                    line = insert(command_index, command_numbers, insert_list)

            elif commands[flag] == 'D':
                flag += 1
                # 제거위치
                if int(commands[flag]) < 10:  # command D 이면서 시행 위치가 인덱스 10이하면 함수 시행행
                    flag += 1
                    # 제거 횟수
                    command_numbers = int(commands[flag])
                    for _ in range(command_numbers):
                        line.pop()
            else:
                flag += 1
                continue
        else:
            flag += 1
    # print(flag)
    print('#{} {}'.format(t + 1, line[0:10]))
