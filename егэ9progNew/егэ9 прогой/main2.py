def t(s):
    a=s.split('.')
    return int(a[0])*2563+int(a[1])*2562+int(a[2])*256+int(a[3])

def ok(a,b,p):
    size=2**(32-p)
    if a//size==b//size: return False
    if a%size in (0,size-1): return False
    if b%size in (0,size-1): return False
    return True

a=t("192.168.106.35"); b=t("192.168.106.117")
L=[p for p in range(1,31) if ok(a,b,p)]
print(min(L), max(L))

a=t("156.77.32.127"); b=t("156.77.117.78")
L=[p for p in range(1,31) if ok(a,b,p)]
print(max(L))