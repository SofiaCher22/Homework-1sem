def tringle(size, symb):
    i = 1
    while i <= size // 2:
        print(i * symb)
        i += 1
    i -= 1
    while i >= 1:
        print(i * symb)
        i -= 1

m = int(input())
p = input()
tringle(m, p)