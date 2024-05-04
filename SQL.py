"""
Модуль осуществляет подключение к базе данных SQL
"""
import os

import pymysql

connection = pymysql.connect(host=os.getenv('BD_HOST'),
                             user='gen_user',
                             password=os.getenv('BD_PASS'),
                             database='favorable_prices')