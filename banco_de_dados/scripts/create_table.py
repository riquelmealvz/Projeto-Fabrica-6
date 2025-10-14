import sqlite3 as sq

DB_PATH = "banco_de_dados/escola_fb.db"

def get_connection():
    return sq.connect(DB_PATH)

def criar_tabela():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_nasc DATE NOT NULL,
                email TEXT unique,
                tel TEXT,
                endereco TEXT NOT NULL,
                curso TEXT NOT NULL,
                status TEXT NOT NULL
            );
        ''')

criar_tabela()