# 9 - 7030
f = open('9_7030.csv')
k = 0
for x in f:
    a = sorted(list(map(int, x.split(';'))))
    q = set(a)
    if len(q) == 3:
        w,e,r = q # распаковываем множество, т.к нельзя обращаться по индексам
        if a.count(w) == 2 and a.count(e) == 2 and a.count(r) == 2:
            qq = sorted(q)
            if qq[0]**2 + qq[1]**2 == qq[2]**2:
                k += 1
print('№1:',k)
f.close()

# 9 - 10091
f = open('10091.txt')
k = 0
for x in f:
    a = sorted(list(map(int, x.split())))
    q = set(a)

    if len(q) == 5:
        kpovt = 0
        knepovt = 0
        spovt = 0
        snepovt = 0
        for xx in q:
            if a.count(xx) == 1:
                knepovt += 1
                snepovt += xx
            elif a.count(xx) == 2:
                kpovt += 2
                spovt += xx * 2
            else:
                break
        else:
            if knepovt == 3 and kpovt == 4:
                if spovt/kpovt < sum(a)/7:
                    k+=1
            
print('№2:',k)
f.close()
# 9 - 7674

f = open('7674.txt')
k = 0
for x in f:
    a = sorted(list(map(int, x.split())))
    q = set(a)
    if len(q) == 4:
        kpovt = 0
        knepovt = 0
        spovt = 0
        snepovt = 0
        for xx in q:
            if a.count(xx) == 1:
                knepovt += 1
                snepovt += xx
            elif a.count(xx) == 2:
                kpovt += 2
                spovt += xx * 2
            else:
                break
        else:
            if knepovt == 3 and kpovt == 2:
                if snepovt/knepovt < spovt/kpovt:
                    k+=1

print('№3:', k)
f.close()
