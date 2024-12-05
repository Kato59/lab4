def find_max_in_2d_array(array):
    return max(max(row) for row in array)

# Пример вызова
array = [[1, 2, 3], [4, 5], [9, 0, -1]]
max_value = find_max_in_2d_array(array)
print(max_value)  # Ожидается: 9
