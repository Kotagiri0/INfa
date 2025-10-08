def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]
x = 2 * 27**7 + 3**10 - 9
s = k(x,3)
print(s.count('0'))
