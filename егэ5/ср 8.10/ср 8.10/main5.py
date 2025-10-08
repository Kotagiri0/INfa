def k(x, base):
    ans = []
    while(x>0):
        ans.append(x%base)
        x//=base
    return ans
x = 4**1503 + 3*4**244 - 2*4**1444 -96
print(sum(k(x, 4)))


