# 비트 연산 연습
n = list(map(int,range(1, 6)))
for i in range(5):
    print(1<<n[i], bin(1<<n[i]))

print(bin(3<<5), 3<<5)
print(bin(4<<5),4<<5)
print(bin(5<<5),5<<5)