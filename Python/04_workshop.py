
#5
# def get_secret_word(args):
#     a_list=[]
#     for i in args:
#         a_list.append(chr(i))
#     a_string = ''.join(a_list)
#     return a_string

# print(get_secret_word([83,115,65,102,89]))

#6
# def get_secret_number(a_string):
#     total =0
#     for i in a_string:
#         total += ord(i)
#     return total

# print(get_secret_number('happy'))

# #7
# def get_strong_word(a_string,b_string):
#     a_total =0
#     b_total =0
#     for i in a_string:
#         a_total += ord(i)
#     for j in b_string:
#         b_total+= ord(j)
#     if a_total >= b_total:
#         return a_string
#     else:
#         return b_string

#print(get_strong_word('delilah','dixon'))