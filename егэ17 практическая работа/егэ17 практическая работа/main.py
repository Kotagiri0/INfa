def d(x):
    x = str(abs(x))
    tmp1 = 0
    tmp2 = 0
    for i in x:
        if(int(i)%2==0):
            tmp1+=1
        else:
            tmp2+=1
    if(tmp1==tmp2):
        return True
    return False
def k(x, y):
    min_a = min(str(x))
    max_b = max(str(y))
    return int(min_a) > int(max_b)
with open('17_7717.txt') as f:
    a = [int(x) for x in f]

s = max([int(x) for x in a if d(x)])
ans1 = []
for i in range(1,len(a)):
    if(k(a[i-1],a[i]) and a[i-1]+a[i]<=s):
        ans1.append(a[i-1]+a[i])
print(len(ans1), max(ans1))