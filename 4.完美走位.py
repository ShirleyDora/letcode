
s=input();m={'A':0,'S':0,'D':0,'W':0}
n=len(s);v=n//4;l=0;r=0;sum=n;f=0
for i in range(n):
    m[s[i]]+=1
for j in m:
    if m[j] > v:
        f+=m[j]-v
if f==0:print(0);exit()
while(1):
    while r-l+1<f:r+=1
    sub=s[l:r+1];copy=m.copy();num=0
    for k in sub:
        if copy[k]>v:
            num+=1;copy[k]-=1
    if num<f:r+=1
    else:sum=min(sum,1+r-l);l+=1
    if r>=n:break
print(sum)
