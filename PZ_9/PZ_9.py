# Исходный словарь
dictionary = {
    "фрукт": "банан",
    "овощ": "морковь"
}
print("Первоначальный словарь:", dictionary)
if dictionary.get("фрукт") != "яблоко":
    dictionary["фрукт"] = "яблоко"
print("Измененный словарь:", dictionary)
