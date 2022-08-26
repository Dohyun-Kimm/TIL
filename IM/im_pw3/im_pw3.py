# IM 준비 암호생성기3
# 2022-08-26

def length(a):
    count = 0
    for _ in range(a):
        count += 1
    return count


# Insert, Delete, Append
# I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.  ex) I 3 2 123152 487651 인덱스 3 앞에 숫자 두개를 집어넣기
# x = index, y= how many, s = strings
def insert(x, y, s):
    global password
    temp = list()  # 옮겨 담을 리스트
    for a in range(N):
        temp.append(password[a])  # 옮겨담기 시작
        if a == x - 1:  # 만약 삽입할 위치가 되면
            for b in range(y):  # 삽입할 리스트의 길이만큼 반복 = y
                temp.append(s[y])  # s = ['6자리','6자리','', '']
    password = temp


# D(삭제) x, y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제한다.[ ex) D 4 4 ]
def delete(x, y):
    global password
    for j in range(y):
        password.pop(x - 1)
    pass


# A(추가) y, s : 암호문의 맨 뒤에 y개의 숫자를 덧붙인다. s는 덧붙일 숫자들이다. [ ex) A 2 421257 796813 ]
def append(y, s):
    global password
    for i in range(length(s)):
        password.append(s[i])
    pass


# 입력 받으면서 함수에 돌려서 결과 값 반영하기

'''
  리스트 형태로 암호문의 각 자리 수를 저장 테스트케이스 1번의 경우 3198
  인덱스 맞추기 위해 함수에 들어갈 숫자는 내부에서 -1 사용함
'''

N = int(input())  # 원본 암호문 길이
password = input().split()  # 원본 암호
M = int(input())  # 명령어 개수
command = input().split()  # 연산들 명령어, 명령어 함수 파라매터가 입력으로 주어짐
command_menu = ['I', 'D', 'A']
command_index = 0
command_numbers = 0
items = list()
flag = 0
while flag < M:
    # I 가 나올 경우 삽입할 인덱스와 개수를 따로 변수에 저장하고 삽입할 숫자들을 리스트의형태로 받아서 함수에 넣기
    if command[flag] == 'I':
        flag += 1
        command_index = int(command[flag])  # 삽입할 위치
        flag += 1
        command_numbers = int(command[flag])  # 삽입 개수
        flag += 1
        for _ in range(command_numbers):  # 목록들
            items.append(command[flag])
            flag += 1
        insert(command_index, command_numbers, items)

    elif command[flag] == 'D':
        flag += 1
        command_index = int(command[flag])  # 삽입할 위치
        flag += 1
        command_numbers = int(command[flag])  # 삽입 개수
        flag += 1
        delete(command_index, command_numbers)

    elif command[flag] == 'A':
        flag += 1
        command_numbers = int(command[flag])  # 삽입 개수
        flag += 1
        for _ in range(command_numbers):  # 목록들
            items.append(command[flag])
            flag += 1
        insert(command_index, command_numbers, items)

    else:
        print('something wrong')

# print(type(password[0]))
# print(edit[0:9])
# 명령어
