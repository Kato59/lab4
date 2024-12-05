def find_max_in_2d_array(array):
    max_value = float('-inf')  # Начальное значение минимальное из возможных
    for row in array:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

# Пример вызова
array = [[1, 2, 3], [4, 5], [9, 0, -1]]
max_value = find_max_in_2d_array(array)
print(max_value)  # Ожидается: 9
