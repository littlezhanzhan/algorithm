str_list = list()
inputString = input()
result = list()
for n in inputString[::-1]:
    result.append(n)

print(''.join(result))