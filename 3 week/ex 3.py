def evk(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 =evk(b, a % b)
    x=y1
    y=x1-(a//b)*y1
    return d, x, y
a=int(input())
b=int(input())
d, x, y = evk(a, b)
print(f"GCD: {d}, x: {x}, y: {y}")