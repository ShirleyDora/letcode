key=input();s=input().split()
num=-1
for i in range(len(s)):
    low=s[i].lower();arr=""
    for j in low:
        if j>='a' and j<='z':
            arr+=j
    l=list(arr);l.sort();arr="".join(l)
    if key==arr:num=i+1;break
print(num)