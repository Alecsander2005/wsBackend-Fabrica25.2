import pymysql

DB_NAME = 'projetomusicas'
USER = 'root'
PASSWORD = '' # sua senha aqui
HOST = 'localhost'

# Conectar sem especificar banco
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD)
cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8mb4'")
print(f"Banco {DB_NAME} criado (ou já existia).")
cursor.close()
conn.close()
