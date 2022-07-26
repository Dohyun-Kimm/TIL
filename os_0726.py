

mass_list = list()
for i in range(5):
    T = input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:')
    if T == 'Done':
        break
    else:
        mass_list.append(list(map(int,T.rstrip('g').split(('%')))))
#print(mass_list)

for idx in range(len(mass_list)):
    amount = (mass_list[idx][0]* mass_list[idx][1]) /100
    #print(f'amount of salt={amount}')
    mass_list[idx].append(amount)

total_amount = 0
total_water = 0
for idx in range(len(mass_list)):
    total_amount += mass_list[idx][2]
    total_water += mass_list[idx][1]

total_mass = str(round((total_amount/total_water)*100,3))
total_water = str(round(total_water,3))
print(f'{total_mass}%{total_water}g')

