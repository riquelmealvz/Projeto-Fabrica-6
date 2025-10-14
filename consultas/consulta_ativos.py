import sqlite3 as sq

DB_PATH = "banco_de_dados/escola_fb.db"

def get_connection():
    return sq.connect(DB_PATH)

def consulta_status():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            SELECT * FROM aluno WHERE status = "ativo"
        ''')
        resultados = cur.fetchall()
        return resultados
    
ativos = consulta_status()

for aluno in ativos:
    print(aluno)