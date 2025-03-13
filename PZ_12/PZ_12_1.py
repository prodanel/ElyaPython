n = int(input("Введите количество элементов в последовательности: "))
sequence = []
for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    sequence.append(num)
half_index = n // 2
if n % 2 != 0:
    half_index += 1
second_half = sequence[half_index:]
sum_of_second_half = sum(second_half)
print(f"Сумма элементов в последней половине последовательности: {sum_of_second_half}")
