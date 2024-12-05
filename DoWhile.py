def sum_do_while(*args):
    result = 0
    index = 0
    if len(args) == 0:  # Проверка на случай отсутствия аргументов
        return 0
    while True:
        result += args[index]
        index += 1
        if index >= len(args):
            break
    return result

# Пример вызова
print(sum_do_while(1, 2, 3))  # 6
print(sum_do_while())         # 0
print(sum_do_while(1, -1, 1)) # 1
