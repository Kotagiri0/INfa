def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]

for x in range(4, 16):
    if( int('13', x) * int('12', x) == int('211', x)):
        print(x)