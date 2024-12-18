import sqlite3
import random
import os

# Удаление старой базы данных, если она существует
if os.path.exists('contacts.db'):
    os.remove('contacts.db')

# Список имен на русском языке
names = [
    "Андрей", "Антон", "Галя", "Мария", "Дмитрий",
    "Елена", "Сергей", "Ольга", "Иван", "Татьяна",
    "Николай", "Анастасия", "Максим", "Екатерина",
    "Павел", "Юлия", "Роман", "Светлана",
    "Александр", "Ксения", "Виктория",
    "Денис", "Маргарита", "Станислав", "Людмила",
    "Владимир", "Тимур", "София", "Алина",
    "Ярослав", "Евгения", "Григорий", "Полина",
    "Наталья", "Михаил", "Кирилл",
    "Дарья", "Арсений", "Ирина",
    "Федор", "Кристина",
    "Елизавета", "Семен",
    "Анатолий", "Зоя"
]
git commit -m "Добавлен документ технической спецификации МК"

# Список доменов для электронной почты
email_domains = [
    "@gmail.com",
    "@yahoo.com",
    "@hotmail.com",
    "@yandex.ru",
    "@mail.ru",
    "@outlook.com",
    "@icloud.com"
]

# Словарь для преобразования русских имен в английский формат
name_to_english = {
    'Андрей': 'Andrey',
    'Антон': 'Anton',
    'Галя': 'Galya',
    'Мария': 'Maria',
    'Дмитрий': 'Dmitry',
    'Елена': 'Elena',
    'Сергей': 'Sergey',
    'Ольга': 'Olga',
    'Иван': 'Ivan',
    'Татьяна': 'Tatiana',
    'Николай': 'Nikolai',
    'Анастасия': 'Anastasia',
    'Максим': 'Maxim',
    'Екатерина': 'Ekaterina',
    'Павел': 'Pavel',
    'Юлия': 'Julia',
    'Роман': 'Roman',
    'Светлана': 'Svetlana',
    'Александр': 'Alexander',
    'Ксения': 'Ksenia',
    'Виктория': 'Victoria',
    'Денис': 'Denis',
    'Маргарита': 'Margarita',
    'Станислав': 'Stanislav',
    'Людмила': 'Lyudmila',
    'Владимир': 'Vladimir',
    'Тимур': 'Timur',
    'София': 'Sofia',
    'Алина': 'Alina',
    'Ярослав': 'Yaroslav',
    'Евгения': 'Evgenia',
    'Григорий': 'Gregory',
    'Полина': 'Polina',
    'Наталья': 'Natalia',
    'Михаил': 'Mikhail',
    'Кирилл': 'Kirill',
    'Дарья': 'Daria',
    'Арсений': 'Arseny',
    'Ирина': 'Irina',
    'Федор': 'Fedor',
    'Кристина': 'Kristina',
    'Елизавета':'Elizabeth',
    'Семен':'Semyon',
     'Анатолий':'Anatoly',
     'Зоя':'Zoya'
}

# Создание новой базы данных и таблицы
connection = sqlite3.connect('contacts.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT,
    phone TEXT,
    email TEXT
)
''')

# Очистка таблицы перед вставкой новых данных (если необходимо)
cursor.execute("DELETE FROM contacts")
connection.commit()

# Генерация и вставка 50 случайных контактов
sample_contacts = []
for _ in range(50):
    name = random.choice(names)  # Случайное имя из списка

    # Исправленный код для генерации телефонного номера с правильными кавычками
    phone = f"8{''.join(random.choices('0123456789', k=10))}"  # Генерация телефонного номера

    english_name = name_to_english[name]  # Получаем английское имя из словаря

    email_domain = random.choice(email_domains)  # Случайный домен из списка

    email = f"{english_name.lower()}{email_domain}"  # Формирование email

    sample_contacts.append((name, phone, email))

cursor.executemany('''
INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)
''', sample_contacts)

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()

print("База данных создана и заполнена 50 контактами.")