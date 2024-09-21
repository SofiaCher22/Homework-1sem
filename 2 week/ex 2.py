
def reverse_groups(G, s):
    # Вычисляем длину группы
    length_of_group = len(s) // G
    
    # Инициализируем список для новых групп
    reversed_groups = []
    
    # Разделяем строку на группы и обращаем их
    for i in range(G):
        start = i * length_of_group
        end = start + length_of_group
        group = s[start:end]
        reversed_group = group[::-1]  # обращаем группу
        reversed_groups.append(reversed_group)
    
    # Склеиваем группы обратно в строку
    result = ''.join(reversed_groups)
    
    return result

# Пример ввода
G =int(input()) 
s =input()
output = reverse_groups(G, s)
print(output)  # Вывод: cbadehgfji