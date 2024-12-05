from functools import reduce

def sum_reduce(*args):
    return reduce(lambda x, y: x + y, args, 0)

# Пример вызова
print(sum_reduce(1, 2, 3))  # 6
print(sum_reduce())         # 0
print(sum_reduce(1, -1, 1)) # 1
