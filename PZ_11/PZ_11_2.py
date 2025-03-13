with open('positive_numbers.txt', 'w') as pos_file:
    pos_file.write('2\n4\n6\n8\n10\n12\n')
with open('negative_numbers.txt', 'w') as neg_file:
    neg_file.write('-1\n-3\n-5\n-7\n-9\n-11\n')
def process_files():
    with open('positive_numbers.txt', 'r') as pos_file:
        positive_numbers = [int(line.strip()) for line in pos_file.readlines()]
    with open('negative_numbers.txt', 'r') as neg_file:
        negative_numbers = [int(line.strip()) for line in neg_file.readlines()]
    even_elements = [num for num in positive_numbers if num % 2 == 0]
    product_of_evens = 1 if even_elements else 0
    for num in even_elements:
        product_of_evens *= num
    min_element = min(positive_numbers)
    odd_elements = [num for num in negative_numbers if num % 2 != 0]
    count_of_odds = len(odd_elements)
    sum_of_odds = sum(odd_elements)
    with open('results.txt', 'w') as result_file:
        result_file.write("Содержимое первого файла:\n")
        result_file.write(f"Четные элементы: {even_elements}\n")
        result_file.write(f"Произведение четных элементов: {product_of_evens}\n")
        result_file.write(f"Минимальный элемент: {min_element}\n")
        result_file.write("\nСодержимое второго файла:\n")
        result_file.write(f"Нечетные элементы: {odd_elements}\n")
        result_file.write(f"Количество нечетных элементов: {count_of_odds}\n")
        result_file.write(f"Сумма нечетных элементов: {sum_of_odds}\n")
process_files()
import string

def process_text_file():
    with open('text18-23.txt', 'r') as text_file:
        lines = text_file.readlines()
    for line in lines:
        print(line.strip())
    punctuation_count = sum(1 for line in lines[:4] for char in line if char in string.punctuation)
    print(f"Количество знаков пунктуации в первых четырех строках: {punctuation_count}")
    with open('lowercase_poem.txt', 'w') as lower_file:
        for line in lines:
            lower_file.write(line.lower())
process_text_file()
