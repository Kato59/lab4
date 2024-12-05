def sum_for_of(*args):
    result = 0
    for num in args:
        result += num
    return result

# Пример вызова
print(sum_for_of(1, 2, 3))  # 6
print(sum_for_of())         # 0
print(sum_for_of(1, -1, 1)) # 1
