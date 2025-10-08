def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]

ans = set()
for n in range(0, 1000):
    s = ''
    if(n% 3 == 0):
        s = '1' + k(n, 3) + '02'
    else:
        s = k(n, 3) + k((n%3)*4,3)
    r = int(s, 3)
    if(r<199):
        ans.add(n)
print(max(ans))