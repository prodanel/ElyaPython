def find_max_positive_multiple_of_4(two_dim_list):
    max_element = None
    for row in two_dim_list:
        for element in row:
            if element > 0 and element % 4 == 0:
                if max_element is None or element > max_element:
                    max_element = element

    return max_element
two_dim_list = [
    [1, -2, 3, 8],
    [4, 16, 5, -12],
    [20, 7, 2, 0],
    [-4, -8, 12, 24]
]

result = find_max_positive_multiple_of_4(two_dim_list)
print("Максимальный положительный элемент, кратный 4:", result)
