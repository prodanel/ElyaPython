import string

def analyze_and_format_text(input_file, output_file):

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    print("Содержимое файла:")
    for line in lines:
        print(line, end='')
    punctuation_count = 0
    for i in range(min(4, len(lines))):
        for char in lines[i]:
            if char in string.punctuation:
                punctuation_count += 1

    print(f"\nКоличество знаков пунктуации в первых четырех строках: {punctuation_count}")
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for line in lines:
                formatted_line = line.lower().strip()
                outfile.write(formatted_line + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

input_file = "text18-23.txt"
output_file = "poem.txt"

with open(input_file, 'w', encoding='utf-8') as f:
    f.write("""И только небо засветилось,
Все шумно вдруг зашевелилось,
Сверкнул за строем строй.
Полковник наш рожден был хватом:
Слуга царю, отец солдатам…
Да, жаль его: сражен булатом,
Он спит в земле сырой.""")

analyze_and_format_text(input_file, output_file)

print(f"Текст в стихотворной форме записан в файл: {output_file}")