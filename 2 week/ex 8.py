a=list(map(int,input().split()))
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[j]<a[i]:
            count+=1
    if count == len(a)//2:
            print(a[i])
            break