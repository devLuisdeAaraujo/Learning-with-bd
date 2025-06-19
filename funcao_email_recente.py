import sqlite3
#Usado para pegar ultima linha email BD
def pegar_linha_mais_recente():
    conexao = sqlite3.connect("cadastre_user.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT email FROM usuarios ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return resultado[0]
    return None
#Usado para pegar ultima linha cpf BD
def pegar_linha_mais_recente_cpf():
    conexao = sqlite3.connect("cadastre_user.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT cpf FROM usuarios ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return resultado[0]
    return None
