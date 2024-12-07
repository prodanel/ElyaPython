number = int(input("Введите трехзначное число: "))

hundreds = number // 100
tens = (number % 100) // 10
units = number % 10

if (hundreds > tens > units) or (hundreds < tens < units):
    print("Да, цифры образуют возрастающую или убывающую последовательность.")
else:
    print("Нет, цифры не образуют возрастающую или убывающую последовательность.")

