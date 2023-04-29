res=0
def dfs(arr, bucket, used, n):
    if used==n or used==len(bucket)*4:
        sum=0
        for i in range(len(bucket)):
            if bucket[i]==0:
                sum+=int(0.8*arr[i])
            else:
                sum+=int(arr[i]+(bucket[i]-1)*arr[i]*0.1)
        global res
        res=max(res,sum)
        return
    for i in range(len(bucket)):
        if bucket[i]<4:
            bucket[i]+=1
            dfs(arr, bucket, used+1, n)
            bucket[i]-=1
m,n=input().split()
m=int(m)
n=int(n)
vec=input().split()
arr=[]
for i in vec:
    arr.append(int(i))
bucket=[]
for i in range(m):
    bucket.append(0)
dfs(arr,bucket,0,n)
print(res)