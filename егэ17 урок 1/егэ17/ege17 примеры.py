'''
k=0
ma = 1015
for i in range(1016, 7938):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and \
       i % 19 != 0 and i % 27 != 0:
        k+=1
        if i > ma:
            ma = i
print(k, ma)
'''
"""
f = open('17-282.txt')
'''a = []
for x in f:
    a.append(int(x))'''
a = [int(x) for x in f]
mi17 = 10001
for x in a:
    if x % 17 == 0 and x < mi17:
        mi17 = x
k = 0
ma_su = 0
for i in range(0, len(a)-1):
    if a[i] % mi17 == 0 or a[i+1] % mi17 == 0:
        k += 1
        if a[i] + a[i+1] > ma_su:
            ma_su = a[i] + a[i+1]
'''for i in range(1, len(a)):
    if a[i] % mi17 == 0 or a[i-1] % mi17 == 0:
        k += 1
        if a[i] + a[i-1] > ma_su:
            ma_su = a[i] + a[i-1]'''
print(k, ma_su)
f.close()
"""
'''
#238
f = open('17-1.txt')
a = [int(x) for x in f]
k = 0
sr = sum(a) / len(a)
ma_su = -99999999
for i in range(2, len(a)):
    count = 0
    if a[i] < sr:
        count+=1
    if a[i-1] < sr:
        count+=1
    if a[i-2] < sr:
        count+=1 
    if count >= 2:
        if abs(a[i]) % 100 == 14 or abs(a[i-1]) % 100 == 14 or abs(a[i-2]) % 100 == 14:
            k+=1
            if a[i] + a[i-1]+ a[i-2] > ma_su:
                ma_su = a[i] + a[i-1]+ a[i-2]
print(k, ma_su)                
f.close()
'''
'''
#338
f = open('17-338.txt')
a = [int(x) for x in f]
k = 0
mi = min(a)
ma_su = -999999999
for i in range(1, len(a)):
    if a[i] % 117 == mi or a[i-1] % 117 == mi:
        k+=1
        if a[i]+a[i-1] > ma_su:
            ma_su = a[i] + a[i-1]
print(k, ma_su)                
f.close()
'''
'''
#241
f = open('17-1.txt')
a = [int(x) for x in f]
k = 0
sr = sum(a) / len(a)
ma_su = -99999999
for i in range(2, len(a)):
    count = 0
    if a[i] < sr:
        count+=1
    if a[i-1] < sr:
        count+=1
    if a[i-2] < sr:
        count+=1 
    if count >= 2:
        count5 = 0
        if str(abs(a[i])).count('5')!= 0:
            count5 += 1
        if str(abs(a[i-1])).count('5')!=0:
            count5+=1
        if str(abs(a[i-2])).count('5')!=0:
            count5+=1
        if count5>=2:
            k+=1
            if a[i] + a[i-1]+ a[i-2] > ma_su:
                ma_su = a[i] + a[i-1]+ a[i-2]
print(k, ma_su)                
f.close()
'''
# 197
f = open('17-10.txt')
a = [int(x) for x in f]
k = 0
mi_su = 20001
for i in range(1, len(a)):
    if 99< a[i]+a[i-1] < 1000 and (a[i]+a[i-1]) % 10 > (a[i]+a[i-1])//10%10:
        k+=1
        if a[i]+a[i-1] < mi_su:
            mi_su = a[i]+a[i-1]
print(k, mi_su)
f.close()








































































