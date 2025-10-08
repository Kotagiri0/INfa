def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]

p = 6 ** 260 + 6 ** 160 + 6**60
for x in range(0, 2031):
    s = p - x
    s = k(s,6)
    if(s.count('0') == 202):
        print(x)


