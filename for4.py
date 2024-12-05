def sum_for(*args):
    result = 0
    for num in args:
        result += num
    return result

# Пример вызова
print(sum_for(1, 2, 3))  # 6
print(sum_for())         # 0
print(sum_for(1, -1, 1)) # 1
