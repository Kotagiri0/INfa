def k(x, base):
    ans = ''
    while(x>0):
        ans+=str(x%base)
        x//=base
    return ans[::-1]


x1 = int('AB', 16)
x2 = int('344', 8)
tmp = 0
print(x1,x2)
for i in range(150, 1000):
    if(i>x1 and i<x2):
        tmp+=1
print(tmp)
