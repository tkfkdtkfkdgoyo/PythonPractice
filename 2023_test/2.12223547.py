input_list = [4,1,3,2,6,5,8,11]

odd_list = []
even_list = []
for i in input_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)


even_list.sort(reverse = True)
odd_list.sort()

output_list = []
for i in range(len(input_list)//2):
    output_list.append(odd_list[i])
    output_list.append(even_list[i])

print('입력(코드 내)')
print(input_list)
print('\n출력')
print(output_list)
