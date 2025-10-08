def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]
x = 7 * 1296**57 - 8* 216**30 + 35

s = k(x,6)
print(s.count('5'))