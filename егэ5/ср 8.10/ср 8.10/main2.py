ans = set()
for n in range(0,1000):
    s = bin(n)[2:]
    if(n%2 == 0):
        s = '1' + s + '11'
    else:
        s = '11' + s + '0'
    r = int(s,2)
    if(r>=500 and r<=1000):
        ans.add(n)
print(len(ans))