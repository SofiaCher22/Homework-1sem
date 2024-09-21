def conv(n,radix):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=""
    while(n>0):
        k=n%radix   # очередная цифра
        r=digits[k]+r # приклеим к результату
        n=n//radix
    return r
 
def vnoc(n,radix):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=0
    for a in n:
        k=digits.index(a)
        r=r*radix+k
    return r
 
N,b=input().split()
N=int(N)
c=int(input())
tmp=vnoc(b,N)
print(conv(tmp,c))