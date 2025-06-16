#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (вар 21).

import tkinter as tk
from tkinter import ttk

def confirm_data():
    print("Данные подтверждены")

def reset_form():
    print("Ввод отменен")


root = tk.Tk()
root.title("Форма регистрации пользователя")

root.configure(padx=20, pady=20, bg="white")

title_label = tk.Label(root, text="Форма регистрации пользователя", font=("Arial", 16), bg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(root, text="Ваше имя:", bg="white")
name_label.grid(row=1, column=0, sticky=tk.E, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

password_label = tk.Label(root, text="Пароль:", bg="white")
password_label.grid(row=2, column=0, sticky=tk.E, pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

age_label = tk.Label(root, text="Возраст:", bg="white")
age_label.grid(row=3, column=0, sticky=tk.E, pady=5)
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

gender_label = tk.Label(root, text="Пол:", bg="white")
gender_label.grid(row=4, column=0, sticky=tk.E, pady=5)

gender = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Мужской", variable=gender, value="Мужской", bg="white")
male_radio.grid(row=4, column=1, sticky=tk.W, padx=(0, 10), pady=5)
female_radio = tk.Radiobutton(root, text="Женский", variable=gender, value="Женский", bg="white")
female_radio.grid(row=4, column=1, sticky=tk.W, padx=(80, 0), pady=5)

hobbies_label = tk.Label(root, text="Ваши увлечения:", bg="white")
hobbies_label.grid(row=5, column=0, sticky=tk.E, pady=5)

music_var = tk.BooleanVar()
music_check = tk.Checkbutton(root, text="Музыка", variable=music_var, bg="white")
music_check.grid(row=5, column=1, sticky=tk.W, padx=(0, 10), pady=5)

video_var = tk.BooleanVar()
video_check = tk.Checkbutton(root, text="Видео", variable=video_var, bg="white")
video_check.grid(row=5, column=1, sticky=tk.W, padx=(80, 10), pady=5)

drawing_var = tk.BooleanVar()
drawing_check = tk.Checkbutton(root, text="Рисование", variable=drawing_var, bg="white")
drawing_check.grid(row=5, column=1, sticky=tk.W, padx=(160, 0), pady=5)

country_label = tk.Label(root, text="Ваша страна:", bg="white")
country_label.grid(row=6, column=0, sticky=tk.E, pady=5)
country_combo = ttk.Combobox(root, values=["Россия", "США", "Германия"])
country_combo.grid(row=6, column=1, sticky=tk.W, pady=5)

city_label = tk.Label(root, text="Ваш город:", bg="white")
city_label.grid(row=7, column=0, sticky=tk.E, pady=5)
city_combo = ttk.Combobox(root, values=["Москва", "Нью-Йорк", "Берлин"])
city_combo.grid(row=7, column=1, sticky=tk.W, pady=5)

about_label = tk.Label(root, text="Кратко о себе:", bg="white")
about_label.grid(row=8, column=0, sticky=tk.E, pady=5)
about_text = tk.Text(root, height=3, width=30)
about_text.grid(row=8, column=1, sticky=tk.W, pady=5)
about_text.insert(tk.END, "краткая информация о ваших увлечениях")

example_label = tk.Label(root, text="Решите пример, запишите результат в поле ниже:", bg="white")
example_label.grid(row=9, column=0, sticky=tk.E, pady=5)
example_entry = tk.Entry(root, width=30)
example_entry.grid(row=9, column=1, sticky=tk.W, pady=5)

reset_button = tk.Button(root, text="Отменить ввод", command=reset_form)
reset_button.grid(row=10, column=0, sticky=tk.E, pady=10, padx=(0,5))

confirm_button = tk.Button(root, text="Данные подтверждаю", command=confirm_data)
confirm_button.grid(row=10, column=1, sticky=tk.W, pady=10, padx=(5,0))

root.mainloop()
