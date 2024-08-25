import time
import psycopg2

# Функция для проверки готовности базы данных
def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="password",
                host="db"
            )
            conn.close()
            print("Database is ready!")
            break
        except psycopg2.OperationalError as e:
            print(f"Database not ready, waiting... Error: {e}")
            time.sleep(2)

# Ожидание готовности базы данных
wait_for_db()

# Подключение к базе данных PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="db"
    )
    cur = conn.cursor()
    print("Connected to the database!")

    # Создание таблицы employees
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INTEGER,
            department VARCHAR(50)
        )
    """)
    print("Table created!")

    # Наполнение таблицы данными
    employees = [
        ('Alice', 30, 'HR'),
        ('Bob', 25, 'Engineering'),
        ('Charlie', 35, 'Sales'),
        ('Donald', 36, 'Desk'),
        ('Evan', 35, 'Engineering'),
        ('Freddie', 48, 'Engineering'),
        ('George', 47, 'Logistics'),
        ('Harald', 30, 'Sales'),
        ('Ilon', 39, 'Logistics'),
        ('George', 57, 'Sales'),
        ('Kelly', 35, 'Desk'),
        ('Lisa', 24, 'Engineering'),
        ('Mary', 46, 'Logistics'),
        ('Naomi', 35, 'Sales'),
        ('Ophra', 33, 'Warehouse'),
        ('Philippe', 47, 'Engineering'),
        ('Quentin', 29, 'Sales'),
        ('Rachel', 35, 'Logistics'),
        ('Susan', 43, 'Desk'),
        ('Tommy', 48, 'Engineering'),
        ('Utah', 19, 'Logistics'),
        ('Vincent', 54, 'Engineering'),
        ('William', 46, 'Warehouse'),
        ('Xiang', 28, 'Desk'),
        ('Yngwie', 34, 'Sales'),
        ('Zoey', 35, 'Logistics'),
    ]

    for emp in employees:
        cur.execute(
            "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)",
            emp
        )
    print("Data inserted!")

    # Вывод данных из таблицы
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

    # Закрытие соединения
    conn.commit()
    cur.close()
    conn.close()
    print("Connection closed!")
except Exception as e:
    print(f"An error occurred: {e}")
