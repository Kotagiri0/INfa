def g(n):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    return int(s, 2)


a = set()
for n in range(50):
    r = g(n)

    a.add(g(r))
    print(g(r))
print(len(a))
