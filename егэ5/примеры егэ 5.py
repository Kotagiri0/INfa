def tri(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
mi = 9999999999999999999
for n in range(1, 10000):
    q = tri(n)
    if n % 3 == 0:
        q += q[-2:]
    else:
        q += tri((n % 3) * 5)
    res = int(q, 3)
    if res > 150:
        if res < mi:
            mi = res
print(mi)
'''for n in range(1000, 10000):
    q = str(n)
    su1 = int(q[0])+int(q[1])
    su2 = int(q[1])+int(q[2])
    su3 = int(q[2])+int(q[3])
    mi,sr,ma = sorted([su1,su2,su3])
    if str(sr)+ str(ma) == '511':
        print(n)
ans = set()'''
'''for n in range(500, 5001):
    q = bin(n)[2:]
    100010101
    q1 = q[1:]
    ind = q1.find('1')
    new2 = q1[:]
    new = int(new2, 2)
    ans.add(n - new)
    if n - new == 0:
        print(q, new2 )
print(len(ans))'''
'''
for n in range(100, 1000):
    a,b,c = sorted([int(x) for x in str(n)])
    ma = c * 10 + b
    mi = a * 10 + b
    if ma - mi == 40 and a != 0 and b != 0 and c != 0:
        print(n)
        break
'''
'''for n in range(1, 10000):
    q = bin(n)[2:]
    if q.count('1') % 2 == 0:
        q += '0'
    else:
        q += '1'
    if q.count('1') % 2 == 0:
        q += '0'
    else:
        q += '1'
    if int(q, 2) > 77:
        print(n)
        break'''
