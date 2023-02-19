# import sqlite3
# from pathlib import Path
#
#
# def db_init():
#     """
#     Создание файла sqlite3
#     """
#     DB_NAME = 'db.sqlite3'
#     DB_PATH = Path(__file__).parent.parent
#     global db, cur
#     db = sqlite3.connect(DB_PATH / DB_NAME)
#     cur = db.cursor()
#
#
# def create_table():
#     """
#     Для создания таблиц
#     """
#     cur.execute(
#         """
#         CREATE TABLE IF NOT EXISTS products (
#             product_id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         price INTEGER,
    #         photo TEXT)
    #     """
    # )
    # cur.execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS orders (
    #         order_id INTEGER PRIMARY KEY,
    #         username TEXT,
    #         adress TEXT,
    #         age INTEGER,
    #         day TEXT,
    #         product_id INTEGER,
    #         FOREIGN KEY (product_id)
    #             REFERENCES products (product_id)
    #             ON DELETE CASCADE)
    #     """
#     )
#     db.commit()
#
#
# def make_full_products():
#     """
#     Заполняем таблицу products
#     """
#     cur.execute("""INSERT INTO products(
#     name,
#     price,
#     photo
#     ) VALUES
#     ('Магнит ада', 1, 'assortiments/magnit-gori-v-adu-s-bananovymi-listyami-scaled.jpg'),
#     ('Магнит преисподни', 1, 'assortiments/neFCfKCmpH3SmoJX.png'),
#     ('Магнит бездны', 1, 'assortiments/n9HkP1gjZyE620yW4lyvkCF1ZIH9KtyfJNFWZwVt-1024x1024.jpeg'),
#     ('Статуэтка Люцифера', 1, 'assortiments/2604061696_w700_h500_kollektsionnaya-statuetka-veronese.webp'),
#     ('Колесо Бафомета', 1, 'assortiments/png-transparent-baphomet-wheel-sigil-of-baphomet-.png'),
#     ('Плакат с суккубами', 1, 'assortiments/3910343172_w600_h600_3910343172.webp'),
#     ('Свитшот демон', 1, 'assortiments/49_3-800x800.jpg'),
#     ('Свитшот "Ад перевыполнен"', 1, 'assortiments/images.jfif'),
#     ('Свитшот "Когда я попаду в ад"', 1, 'assortiments/62228_Svitshot_Kogda_ya_popadu_v_ad_.jpg')
#     """)
#     db.commit()

#
# def get_products():
#     """
#     Достаём данные из products
#     """
#     cur.execute("""
#     SELECT * FROM products
#     """)
#     return cur.fetchall()
#
#
# def make_full_order(data):
#     """
#         Заполняем таблицу order
#     """
#     data = data.as_dict()
#     cur.execute("""INSERT INTO orders(
#         username,
#         adress,
#         age,
#         day,
#         product_id
#     ) VALUES (:user_name,:adress,:age,:day,:product_id)""",
#                 {'user_name': data['name'],
#                 'adress': data['adress'],
#                  'age': data['age'],
#                  'day': data['day'],
#                  'product_id': data['product_id']})
#     db.commit()

# import os
# dirname= input('имя папки:')
# os.mkdir(dirname)