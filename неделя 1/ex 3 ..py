a=list(map(int, input().split()))
v=1
for i in len(a):
    v*=a[i]
m=v**(1/len(a))
print(m)
