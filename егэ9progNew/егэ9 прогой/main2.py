f = open("9778.txt")
k=[]
tmp=1
for s in f:
    a = list(map(int, s.split()))
    rep=[]
    nrep= []
    for x in a:
        if(a.count(x) == 2):
            rep.append(x)
        elif(a.count(x) == 1):
            nrep.append(x)
    if(len(rep)==2 and len(nrep)==4 and rep[0]>=(sum(nrep)/len(nrep))):
        k.append(tmp)
        #print(tmp)
        #break
    tmp+=1
print(min(k))



