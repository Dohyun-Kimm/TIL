#연속된 값은 지우기.
# for enumerate if
#입력 예시 [1,1,3,3,0,1,1]

N = input()
N = N[1::2]
M= list()
for i in range(len(N)):
    M.append(int(N[i]))

# [1,1,3,3,0,1,1]
# for idx, num in enumerate(M):
#     if idx == len(M):
#         break
#     if M[idx] == M[idx+1]:
#         print(f'idx:{idx},M:{M[idx]}')
#         print(f'idx:{idx+1},M:{M[idx+1]}')
#         M.remove(M[idx+1])
#         print(M)
L= list()
for idx, num in enumerate(M):
    if idx + 1 < len(M):
        #print(f'dix:{idx}')
        if M[idx] == M[idx+1]:
            continue
        L.append(M[idx])
    if idx == len(M)-1 and num == M[idx-1]:
        L.append(M[idx])
    
    
print(L)