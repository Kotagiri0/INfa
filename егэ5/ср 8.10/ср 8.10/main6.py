def k(x, base):
    ans = []
    while(x>0):
        ans.append(x%base)
        x//=base
    return ans
def f(x):
    tmp = True
    for i in x:
        if(int(i) %2 ==1):
            return False
    return True
tmp = 0
for base in range(2,11):
    if(f(k(3456,base))):
        tmp+=base
        print(base)
print()

