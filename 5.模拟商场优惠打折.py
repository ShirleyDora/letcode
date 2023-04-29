import copy
m,n,k= map(int, input().split())
x=int(input())
prices=[int(input()) for _ in range(x)]
def use_T1(ticket,res):
    tmp=res[0]
    while tmp>=100 and ticket>0:
        res[0]-=10;res[1]+=1;ticket-=1;tmp-=100
    return(res) 
def use_T2(ticket,res):
    if ticket>0:
        res[0]=int(res[0]*0.92);res[1]=1
    return res
def use_T3(ticket,res):
    while ticket>0 and res[0]>=5:
        res[0]-=5;ticket-=1;res[1]+=1
    return res
for price in prices:
    res1=use_T1(m,[price,0])
    res2=use_T2(n,[price,0])
    res3=use_T3(k,[price,0])
    result=[float('inf'),float('inf')]
    if price<100:
        result=use_T3(k,res2)
        print(*result)
        continue
    else:
        if res1[0]<=res2[0]:
            tmp_res=copy.copy(res1)
            r2=use_T2(n,res1)
            r3=use_T3(k,tmp_res)
            result=r2 if r2[0]<=r3[0] else r3
        else:
            tmp_res = copy.copy(res2)
            r1 = use_T1(m, res2)
            r3 = use_T3(k, tmp_res)
            result=r1 if r1[0]<=r3[0] else r3
        print(*result)