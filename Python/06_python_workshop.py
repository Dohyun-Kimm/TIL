
# a = [1,1,1,2,2,2,3,3]

# a = list(set(a))
# print(a)
#homework
#1
# a_list = [1,5,7,4]
# print(f'sorted():{sorted(a_list)}')
# print(f'.sort(): {a_list.sort()}')

# a = [1, 2, 3, 4, 5]
# b = a
# a[2] = 5
# print(a)
# print(b)

# def duplicated_letters(a_string):

#     new_list = list()
#     for i in a_string:
#         if a_string.count(i) > 1:
#             if i in new_list:
#                 continue
#             else:
#                 new_list.append(i)
    
#     return new_list
# print(duplicated_letters('apple'))
# print(duplicated_letters('banana'))


# def low_and_up(a):
#     pass
#     new_string = ''
#     for i in range(len(a)):
#         if i % 2==0:
#             new_string += a[i].lower()
#         else:
#             new_string += a[i].upper()
#     return new_string

# print(low_and_up('apple'))
# print(low_and_up('banana'))

# def lonely(a_list):
    
#     cnt =1
#     while True:
#         #print(f'{a_list[cnt]} == {a_list[cnt-1]}')
#         if cnt == len(a_list)-1:
            
#             if a_list[cnt] == a_list[cnt-1]:
            
#                 a_list.pop(cnt-1)
#             break
        
#         elif a_list[cnt] == a_list[cnt-1]:
#             a_list.remove(a_list[cnt])
            
#             cnt =1
#         else : 
#             cnt +=1
            
        
#     return a_list

# print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
# print(lonely([4, 4, 4, 3, 3])) # => [4, 3]

def my_find(text, alphabet):
    ind = list()
    while True:
        if len(ind) == 0 and text.find(alphabet)==-1:
            return -1
        elif text.find(alphabet) != -1:
            ind.append(text.find(alphabet))
            text = text.strip(alphabet)
        elif text.find(alphabet)==-1:
            break
    return ind
        
print(my_find('apple', 'p'))
print(my_find('a', 'p'))