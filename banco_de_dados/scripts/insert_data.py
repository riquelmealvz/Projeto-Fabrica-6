import sqlite3 as sq

DB_PATH = "banco_de_dados/escola_fb.db"

def get_connection():
    return sq.connect(DB_PATH)

def inserir_aluno(nome, data_nasc, email, tel, endereco, curso, status):
    with get_connection() as conn:
        cur = conn.cursor()
        conn.execute('INSERT INTO aluno (nome, data_nasc, email, tel, endereco, curso, status) VALUES (?, ?, ?, ?, ?, ?, ?)', (nome, data_nasc, email, tel, endereco, curso, status))

        conn.commit()
   
if __name__ == "__main__":
    nome = input("Digite o nome do aluno: ")
    data = input("Digite a data de nascimento (YYYY-MM-DD): ")
    email = input("Digite o email do aluno: ")
    tel = input("Digite o telefone do aluno: ")
    endereco = input("Digite o endereço: ")
    curso = input("Digite o curso do aluno: ")
    status = input('Digite o status da matricula (ex: "Ativo", "Finalizado", "Trancado", "Cancelado"): ')

    inserir_aluno(nome, data, email, tel, endereco, curso, status)