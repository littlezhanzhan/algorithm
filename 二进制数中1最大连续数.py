num = bin(int(input())).replace("0b", "")

res = 0
# print(num)
for i in range(1, len(num)+1):
    if '1'*  i in num:
        res = i
    else:
        break
print(res)



