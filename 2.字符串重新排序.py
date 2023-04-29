v=input().split();arr=[];m={};lar=0
for i in v:
    l=list(i);l.sort();t="".join(l);arr.append(t)
for i in arr:
    if i not in m:
        m[i]=0
    m[i]+=1;lar=max(lar,m[i])
for i in range(lar,0,-1):
    s=[]
    for j in m:
        if m[j]==i:s.append(j)
    s=sorted(s, key=lambda x:(len(x),x))
    for w in s:
        for k in range(i):
            print(w+" ",end="")