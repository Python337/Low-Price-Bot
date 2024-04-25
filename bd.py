from SQL import connection
def feather_drills(b):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Feather_drills')

    rows = cursor.fetchall()
    a = ''
    for line in rows:
        if line[0] == b:
            a += f'{line[1]}\n\n'
            a += f'{line[2]}\n\n'
            a += f'{line[3]}\n\n'
            a += f'{line[4]}\n\n'
            a += f'{line[5]}\n\n'
            return a

# Извлечение информации из базы данных "favorable_prices" и таблицы "Feather_drills"
#
# Введена команда, которая открывает таблицу "Discs_for_grinder".
# В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
# Потом эти все данные возвращаются с помощью return.

def spiral_drills(b):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Spiral_drills')

    rows = cursor.fetchall()
    a = ''
    for line in rows:
        if line[0] == b:
            a += f'{line[1]}\n\n'
            a += f'{line[2]}\n\n'
            a += f'{line[3]}\n\n'
            a += f'{line[4]}\n\n'
            a += f'{line[5]}\n\n'
            return a

# Извлечение информации из базы данных "favorable_prices" и таблицы "Discs_for_grinder"
#
# Введена команда, которая открывает таблицу "Discs_for_grinder".
# В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
# Потом эти все данные возвращаются с помощью return.

def discs_for_grinder(b):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Discs_for_grinder')

    rows = cursor.fetchall()
    a = ''
    for line in rows:
        if line[0] == b:
            a += f'{line[1]}\n\n'
            a += f'{line[2]}\n\n'
            a += f'{line[3]}\n\n'
            a += f'{line[4]}\n\n'
            a += f'{line[5]}\n\n'
            return a

# Извлечение информации из базы данных "favorable_prices" и таблицы "Discs_for_grinder"
#
# Введена команда, которая открывает таблицу "Discs_for_grinder".
# В функцию подставляется id товара и все его данные из столбиков извлекаются с помощью цикла for.
# Потом эти все данные возвращаются с помощью return.
