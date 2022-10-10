def isprime(a):
    for i in range(2,a):
        if a %i ==0:
            return False
    else:
        return True

T = int(input())

#num =list() # 입력숫자들
prime_list = list()
prime_pair = list()

for _ in range(T):
    i = int(input())
    for j in range(2,(i)//2+1):
        if isprime(j) ==True:
            remain = i -j
            if isprime(remain) ==True:
                prime_pair=[j,remain]
    prime_list.append(prime_pair)

    #num.append(i)
#  소수 구하는 함수


# 소수의 합으로 구성되는지 확인 하는 반복문 + 차이가 적은 쌍을 업데이트
#출력 형식에 맞게 출력하기
for idx in range(len(prime_list)):
    print(' '.join(map(str,prime_list[idx])))





