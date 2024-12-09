# После долгих запросов SQL и разных попыток почистить данные, получился новый файл my1database.s3db
import pandas as pd 
import sqlite3

# Указываем пути к файлам
users_file = 'users1.csv' 
log_file = 'log1.csv' 
database_file = 'database.s3db'

# Создаем базу данных SQLite
conn = sqlite3.connect(database_file) 
cursor = conn.cursor()

# Создаем схему базы данных
with open('schema.sql', 'r') as schema_file: schema_sql = schema_file.read() 
cursor.executescript(schema_sql)

# Загружаем данные из users1.csv
users_df = pd.read_csv(users_file, encoding='koi8_r')

# Загружаем данные в таблицу USERS
users_df.to_sql('USERS', conn, if_exists='replace', index=False)

# Загружаем данные из log1.csv
log_df = pd.read_csv(log_file)

# Заменяем названия столбцов для соответствия
log_df.rename(columns={'user_id': 'user_id', 'time': 'time', 'bet': 'bet', 'win': 'win'}, inplace=True)

# Загружаем данные в таблицу LOG
log_df.to_sql('LOG', conn, if_exists='replace', index=False)

# Завершение работы с базой данных
conn.commit() 
conn.close()

print("Данные успешно загружены в базу данных.")