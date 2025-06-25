#Приложение ПРОКАТ АВТОМОБИЛЕЙ для некоторой организации. БД должна
#содержать таблицу Клиент со следующей структурой записи: ФИО клиента, марка авто,
#срок проката, сумма, предоплата (да/нет).

import sqlite3

conn = sqlite3.connect('car_rental.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    car_brand TEXT NOT NULL,
    rental_period INTEGER NOT NULL,  -- срок проката в днях
    amount REAL NOT NULL,             -- сумма
    prepayment BOOLEAN NOT NULL        -- предоплата (да/нет)
)
''')

conn.commit()
conn.close()

def add_client(full_name, car_brand, rental_period, amount, prepayment):
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Client (full_name, car_brand, rental_period, amount, prepayment)
    VALUES (?, ?, ?, ?, ?)
    ''', (full_name, car_brand, rental_period, amount, prepayment))

    conn.commit()
    conn.close()

def display_clients():
    conn = sqlite3.connect('car_rental.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Client')
    clients = cursor.fetchall()

    for client in clients:
        print(f'ID: {client[0]}, ФИО: {client[1]}, Марка авто: {client[2]}, '
              f'Срок проката: {client[3]} дней, Сумма: {client[4]}, '
              f'Предоплата: {"Да" if client[5] else "Нет"}')

    conn.close()
if __name__ == "__main__":

    add_client("Иванов Иван Иванович", "Toyota Camry", 7, 3500.0, True)
    add_client("Петров Петр Петрович", "Honda Accord", 5, 2500.0, False)

    print("Список клиентов:")
    display_clients()



