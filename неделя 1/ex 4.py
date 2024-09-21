lines=f.readlines()
a=list(map(readlines[0].split()))
op=lines(1)
if op=='+':
    res=sum(a)
elif op=='-':
    for i in a[1:]:
        res-=i
else:
    for i in a:
        res*=i
    
f.close()
f.open('output.txt', 'w')
f.write(str(res))
f.close()