toys = ["мяч", "кукла", "конструктор", "машинка", "пазл"]

kindergarten_1 = ["мяч", "кукла" , "конструктор"]
kindergarten_2 = ["конструктор", "мяч" "пазл"]
kindergarten_3 = ["машинка", "пазл", "мяч"]

all_toys_in_kindergartens = set(kindergarten_1) | set(kindergarten_2) | set(kindergarten_3)
toys_not_in_any_kindergarten = set(toys) - all_toys_in_kindergartens
toys_in_all_kindergartens = set(kindergarten_1) & set(kindergarten_2) & set(kindergarten_3)

print("Игрушки, которых нет ни в одном детском саду:", toys_not_in_any_kindergarten)
print("Игрушки, которые есть в каждом детском саду:", toys_in_all_kindergartens)

