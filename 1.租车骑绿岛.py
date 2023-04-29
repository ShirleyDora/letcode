m, n = map(int, input().split())
arr=sorted(map(int, input().split()))
l=0;r=n-1;sum=0
while l<=r:
    if arr[l]+arr[r]<=m:
        l+=1
    r-=1;sum+=1
print(sum)