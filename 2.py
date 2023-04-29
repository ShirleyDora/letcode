v = input().split()
arr = [''.join(sorted(i)) for i in v]
m = {i: arr.count(i) for i in set(arr)}
for i in range(max(m.values()), 0, -1):
    s = sorted([j for j in m if m[j] == i], key=lambda x: (len(x), x))
    print(' '.join([w for w in s for k in range(i)]), end=' ')
