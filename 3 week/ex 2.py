def prime(n):
    f=[]
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            f.append(divisor)
            n //= divisor
        divisor += 1
    return f
k = int(input())
result=prime(k)
print(f"Простые множители числа {k}: {result}")