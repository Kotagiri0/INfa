print('задача 5')
def sum_digit(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

count = 1
print(bin(123456789))
print(bin(1987654321))
#0b111010110111100110100010101
# 0b1110110011110010011001010110001
# уберем 3 последних разряда и переведем обратно в 10 сс
a = int('111010110111100110100010',2)
b = int('1110110011110010011001010110',2)
print(a, b) # потенциальные исходники, которые дают R в нужном диапазоне
# определим точнее
for i in range(a,b+1,1):
    n = bin(i)[2:]
    if sum_digit(i) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if sum_digit(r) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if sum_digit(r) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if 123456789<=r<=1987654321:
        print(i,'ok, left')
        left = i
        break

for i in range(b,a-1,-1):
    n = bin(i)[2:]
    if sum_digit(i) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if sum_digit(r) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if sum_digit(r) % 2 == 1:
        n += '1'
    else:
        n += '0'
    r = int(n, 2)
    if 123456789<=r<=1987654321:
        print(i,'ok, right

        
        right = i
        break
print('ответ', right - left + 1)
