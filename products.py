import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price INTEGER NOT NULL,
    product_availability TEXT NOT NULL
);
'''

cursor.execute(create_table_query)

insert_user_queries = [
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Iphone 15 pro', 'Смартфоны', 125000, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Sony PlayStation 5 Slim', 'Игровые консоли', 65000, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Dyson V10 Absolute', 'Пылесосы', 56000, 'Нет');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Samsung Galaxy Z Flip 5', 'Смартфоны', 104500, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Apple iPad Mini', 'Планшеты', 67000, 'Нет');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Apple MacBook Pro 14', 'Ноутбуки', 350000, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Lenco LS-50WD', 'Виниловые проигрыватели', 15000, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Apple AirPods Max', 'Беспроводные наушники', 75000, 'Да');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Apple iPhone 15 Clear Case', 'Чехлы', 7000, 'Нет');"),
    ("INSERT INTO products (product_name, category, price, product_availability) VALUES ('Apple USB-C Charger Cable', 'Кабели для смартфонов', 2500, 'Нет');"),
]

for query in insert_user_queries:
    cursor.execute(query)

conn.commit()

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
print(rows)

conn.close()