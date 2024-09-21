a=list(map(int, input().split()))
unique_list = []
for i in range(len(a)+2):
    if a.count(i)==1:
        unique_list.append(i)
print(unique_list)