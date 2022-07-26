# 홀수번째로 입력되는 값들끼리 방향이 같고
# 짝수번째로 입력되는 값들끼리 방향이 같다.
#좌표로 모든점 받기 상(4,y+) , 우(1,x+) + // 하(3,y-) 좌 (2,-x)-

per_land = int(input())
coor = [0,0]
way = list()
#6좌표 구하기
for _ in range(6):
    T = list(map(int,input().split(' ')))
    way.append(T)

print(way)
farm = list()
for i in way:
    #print(type(i[0]))
    if i[0] ==4 :
        coor[1] += i[1]
        farm.append(coor)
    if i [0] ==3:
        coor[1] -= i [1]
        farm.append(coor)
print(farm)
