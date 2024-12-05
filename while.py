def sum_while(*args):
    result = 0
    index = 0
    while index < len(args):
        result += args[index]
        index += 1
    return result

# Пример вызова
print(sum_while(1, 2, 3))  # 6
print(sum_while())         # 0
print(sum_while(1, -1, 1)) # 1
