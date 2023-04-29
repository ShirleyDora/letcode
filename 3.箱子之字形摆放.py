str,n=input().split();n=int(n);arr=[]
for i in range(n):
    t=[];arr.append(t)
for i in range(len(str)):
    if int(i/n)&1==0:
        v=i%n;arr[v].append(str[i])
    else:
        v=(n-1)-i%n;arr[v].append(str[i])
for i in arr:
    for w in i:
        print(w,end="")
    print()