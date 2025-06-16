import random
def generate_files():
    with open('positive_numbers.txt', 'w') as pos_file:
        pos_numbers = [random.randint(1, 100) for _ in range(10)]
        pos_file.write(' '.join(map(str, pos_numbers)))
    with open('negative_numbers.txt', 'w') as neg_file:
        neg_numbers = [random.randint(-100, -1) for _ in range(10)]
        neg_file.write(' '.join(map(str, neg_numbers)))
def process_files():
    with open('positive_numbers.txt', 'r') as pos_file:
        pos_numbers = list(map(int, pos_file.read().strip().split()))
    even_numbers = [num for num in pos_numbers if num % 2 == 0]
    product_of_evens = 1 if even_numbers else 0
    for num in even_numbers:
        product_of_evens *= num
    min_positive = min(pos_numbers) if pos_numbers else None
    with open('negative_numbers.txt', 'r') as neg_file:
        neg_numbers = list(map(int, neg_file.read().strip().split()))
    odd_numbers = [num for num in neg_numbers if num % 2 != 0]
    count_of_odds = len(odd_numbers)
    sum_of_odds = sum(odd_numbers)
    with open('results.txt', 'w') as result_file:
        result_file.write("Содержимое первого файла:\n")
        result_file.write("Четные элементы: " + ' '.join(map(str, even_numbers)) + '\n')
        result_file.write("Произведение четных элементов: " + str(product_of_evens) + '\n')
        result_file.write("Минимальный элемент: " + str(min_positive) + '\n')

        result_file.write("\nСодержимое второго файла:\n")
        result_file.write("Нечетные элементы: " + ' '.join(map(str, odd_numbers)) + '\n')
        result_file.write("Количество нечетных элементов: " + str(count_of_odds) + '\n')
        result_file.write("Сумма нечетных элементов: " + str(sum_of_odds) + '\n')
if __name__ == "__main__":
    generate_files()
    process_files()
