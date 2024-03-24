# import pymysql
#
#
# connection = pymysql.connect(host='147.45.105.54',
#                              user='gen_user',
#                              password='mfohmdu%E3$b\k',
#                              database='favorable_prices',
# )
#
#
# def feather_drill():
#     with connection:
#         cursor = connection.cursor()
#         cursor.execute('SELECT * FROM Construction_goods')
#         rows = cursor.fetchall()
#         a = ''
#         for line in rows:
#             i = 0
#             a += f'{line[i]}\n'
#             i += 1
#         return a
