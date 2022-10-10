#기둥 개수
#왼쪽면의 위치를 나타내는 정수 L
#높이 H
# 튜플을 원소로 하는 리스트?

T = int(input())
x=[]
y =[]
for i in range(T):
    t = input()
    t1= t.split(' ')
    x.append(int(t1[0]))
    y.append(int(t1[1]))

width = max(x)-min(x)
height = max(y)

largest = width * height

print(largest)

    