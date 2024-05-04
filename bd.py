"""
Модуль осуществляет поиск в базе данных по заданным характеристикам
"""
from SQL import connection


def feather_drills(id):
    """
    Извлечение информации из базы данных "favorable_prices" и таблицы "Feather_drills"

    Введена команда, которая открывает таблицу "Discs_for_grinder".
    В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
    Потом эти все данные возвращаются с помощью return.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Feather_drills')

    rows = cursor.fetchall()
    information_database = ''
    for line in rows:
        if line[0] == id:
            information_database += f'{line[1]}\n\n'
            information_database += f'{line[2]}\n\n'
            information_database += f'{line[3]}\n\n'
            information_database += f'{line[4]}\n\n'
            information_database += f'{line[5]}\n\n'
            return information_database


def spiral_drills(id):
    """
    Извлечение информации из базы данных "favorable_prices" и таблицы "Discs_for_grinder"

    Введена команда, которая открывает таблицу "Discs_for_grinder".
    В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
    Потом эти все данные возвращаются с помощью return.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Spiral_drills')

    rows = cursor.fetchall()
    information_database = ''
    for line in rows:
        if line[0] == id:
            information_database += f'{line[1]}\n\n'
            information_database += f'{line[2]}\n\n'
            information_database += f'{line[3]}\n\n'
            information_database += f'{line[4]}\n\n'
            information_database += f'{line[5]}\n\n'
            return information_database


def discs_for_grinder(id):
    """
    Извлечение информации из базы данных "favorable_prices" и таблицы "Discs_for_grinder"

    Введена команда, которая открывает таблицу "Discs_for_grinder".
    В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
    Потом эти все данные возвращаются с помощью return.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Discs_for_grinder')

    rows = cursor.fetchall()
    information_database = ''
    for line in rows:
        if line[0] == id:
            information_database += f'{line[1]}\n\n'
            information_database += f'{line[2]}\n\n'
            information_database += f'{line[3]}\n\n'
            information_database += f'{line[4]}\n\n'
            information_database += f'{line[5]}\n\n'
            return information_database
