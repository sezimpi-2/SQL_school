import sqlite3

def setup_database():

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL)''')

    countries_data = [('Кыргызстан',), ('Германия',), ('Китай',)]
    cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries_data)

    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        area REAL DEFAULT 0,
                        country_id INTEGER,
                        FOREIGN KEY (country_id) REFERENCES countries(id))''')

   
    cities_data = [('Бишкек', 123.45, 1),
                   ('Ош', 90.2, 2),
                   ('Берлин', 891.85, 3),
                   ('Пекин', 1641.8, 4),
                   ('Москва', 2561.0, 5), 
                   ('Лондон', 1572.0, 7),  
                   ('Нью-Йорк', 1214.0, 7)] 
    cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities_data)

   
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        city_id INTEGER,
                        FOREIGN KEY (city_id) REFERENCES cities(id))''')
    students_data = [('Иван', 'Иванов', 1),
                     ('Петр', 'Петров', 2),
                     ('Мария', 'Сидорова', 3),
                     ('Александр', 'Смирнов', 4),  
                     ('Екатерина', 'Иванова', 5),  
                     ('Андрей', 'Петров', 6),  
                     ('Светлана', 'Сидорова', 7),  
                     ('Дмитрий', 'Смирнов', 1),
                     ('Ольга', 'Иванова', 2),  
                     ('Игорь', 'Петров', 3),  
                     ('Наталья', 'Сидорова', 4),  
                     ('Владимир', 'Смирнов', 5),  
                     ('Татьяна', 'Иванова', 6),  
                     ('Сергей', 'Петров', 7), 
                     ('Елена', 'Сидорова', 1),  
                     ('Анна', 'Смирнова', 2),
                    ]
    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students_data)

 
    conn.commit()
    conn.close()

setup_database()
