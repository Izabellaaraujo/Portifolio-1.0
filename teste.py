from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

def connection(server, database):
    conn = pyodbc.connect(
        f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};trusted_connection=yes"
    )
    return conn

server = os.getenv("SERVER_PORTFOLIO")
database = os.getenv("DATABASE_PORTFOLIO")
conn = connection(server, database)

if conn:
    print("Conexão bem-sucedida!")
else:
    print("Erro ao conectar ao banco de dados.")