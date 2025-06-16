#Разработать программу с применением пакета tk, взяв в качестве условия эту задачу: "Дан словарь с произвольным количеством элементов.
#Выяснить имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
#добавить его в словарь. Вывести на экран первоначальный словарь и измененный."

import tkinter as tk
from tkinter import ttk
import json

def process_dictionary():

    global original_dict
    global result_text

    try:
        key_exists = False
        for key, value in original_dict.items():
            if key == "фрукт" and value == "яблоко":
                key_exists = True
                break

        if not key_exists:
            original_dict["фрукт"] = "яблоко"
            message = "Элемент 'фрукт = яблоко' добавлен в словарь."
        else:
            message = "Элемент 'фрукт = яблоко' уже существует в словаре."

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Первоначальный словарь:\n")
        result_text.insert(tk.END, json.dumps(original_dict, indent=4, ensure_ascii=False) + "\n\n")
        result_text.insert(tk.END, "Измененный словарь:\n")
        result_text.insert(tk.END, json.dumps(original_dict, indent=4, ensure_ascii=False) + "\n\n")
        result_text.insert(tk.END, message)

    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Произошла ошибка: {e}")


def create_example_dictionary():
    global original_dict
    original_dict = {
        "овощ": "морковь",
        "цвет": "оранжевый",
        "число": 42
    }

root = tk.Tk()
root.title("Обработка словаря")

original_dict = {}

create_example_dictionary()

process_button = ttk.Button(root, text="Обработать словарь", command=process_dictionary)
process_button.pack(pady=10)

result_text = tk.Text(root, height=20, width=60)
result_text.pack(pady=10)

root.mainloop()
