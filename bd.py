from SQL import connection

def get(b):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Construction_goods')

    rows = cursor.fetchall()
    a = ''
    for line in rows:
        if line[0] == b:
            a += f'{line[1]}\n\n'
            a += f'{line[2]}\n\n'
            a += f'{line[3]}\n\n'
            a += f'{line[4]}\n\n'
            a += f'{line[6]}\n\n'
            return a

