import random

def generate_numbers(filename, count, positive_only):
    with open(filename, 'w') as f:
        for _ in range(count):
            if positive_only:
                num = random.randint(1, 100)  # Только положительные числа
            else:
                num = random.randint(-100, 100) # Положительные и отрицательные
            f.write(str(num) + '\n')

def process_numbers(file1, file2, output_file):
    even_numbers = []
    odd_numbers = []

    try:
        with open(file1, 'r') as f1:
            numbers1 = [int(line.strip()) for line in f1]
    except FileNotFoundError:
        print(f"Ошибка: Файл {file1} не найден.")
        return
    except ValueError:
        print(f"Ошибка: В файле {file1} обнаружены некорректные данные (не целые числа).")
        return

    try:
        with open(file2, 'r') as f2:
            numbers2 = [int(line.strip()) for line in f2]
    except FileNotFoundError:
        print(f"Ошибка: Файл {file2} не найден.")
        return
    except ValueError:
        print(f"Ошибка: В файле {file2} обнаружены некорректные данные (не целые числа).")
        return

    for num in numbers1:
        if num % 2 == 0:
            even_numbers.append(num)

    for num in numbers2:
        if num % 2 != 0:
            odd_numbers.append(num)

    product_even = 1
    if even_numbers:
        for num in even_numbers:
            product_even *= num
        min_even = min(even_numbers)
    else:
        product_even = 0
        min_even = "Нет четных чисел"

    count_odd = len(odd_numbers)
    sum_odd = sum(odd_numbers)

    with open(output_file, 'w') as outfile:
        outfile.write("Содержимое первого файла:\n")
        outfile.write(f"Четные элементы: {even_numbers}\n")
        outfile.write(f"Произведение четных элементов: {product_even}\n")
        outfile.write(f"Минимальный элемент: {min_even}\n")

        outfile.write("\nСодержимое второго файла:\n")
        outfile.write(f"Нечетные элементы: {odd_numbers}\n")
        outfile.write(f"Количество нечетных элементов: {count_odd}\n")
        outfile.write(f"Сумма нечетных элементов: {sum_odd}\n")

file1 = "positive_numbers.txt"
file2 = "negative_numbers.txt"
output_file = "result.txt"

generate_numbers(file1, 10, True)
generate_numbers(file2, 10, False)

process_numbers(file1, file2, output_file)

print(f"Результаты записаны в файл: {output_file}")