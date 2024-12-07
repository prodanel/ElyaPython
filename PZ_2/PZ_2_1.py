def get_hundreds_digit(number):
    if number <= 999:
        raise ValueError("Число должно быть больше 999.")

    hundreds_digit = (number // 100) % 10
    return hundreds_digit

number = 1234
print(get_hundreds_digit(number))
