import sqlite3
from validate_docbr import CPF
import re
import hashlib
class Conectar:
    def create_table(self):
        #Cria os valores no banco de dados
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                codigo TEXT
                
            )
        """)
        conexao.commit()
        conexao.close()
    #insere os valores no banco de dados no seu respectitivo valor
    def insert_data(self, nome, cpf, email, senha):
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nome, cpf, email, senha)
            VALUES (?, ?, ?, ?)
        """, (nome, cpf, email, senha))
        conexao.commit()
        conexao.close()
    #Obtem os dados do banco de dados
    def obtain_data(self):
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
        conexao.close()
        return dados
    #funcao para validar o cpf, no qual eu uso a biblioteca para cpfBrasileiros
    def validar_cpf(cpf:str)->bool:
        cpf_obj = CPF()
        return cpf_obj.validate(cpf)
    #para vizualizar e entregar se o cpf ja é cadastrado
    def cpf_existe(self,cpf):
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE cpf = ?",(cpf,))
        resultado = cursor.fetchone()
        conexao.close()
        return resultado is not None
    #validacao do email usando biblioteca regex
    def validate_email(email:str)->bool:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return (re.match(email_pattern,email))
    #caso o email ja exista no banco de dados
    def email_existe(self,email):
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?",(email,))
        resultado = cursor.fetchone()
        conexao.close()
        return resultado is not None
    #criptografa a senha
    def senha_criptografada(self,senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    #verifica se a senha possue caracteres corretos
    def verificar_senha(senha:str)->bool:
        minimo_senha = 8
        letras_maiusculas = 1
        letras_minusculas = 1
        numeros_minimo = 1

        count_caracter_especial = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', senha))
        count_numeros = len(re.findall(r'\d', senha))
        count_letras_maiuscula = len(re.findall(r'[A-Z]', senha))
        count_letras_minusculas = len(re.findall(r'[a-z]', senha))
        

        if (
            len(senha) >= minimo_senha and
            count_caracter_especial >= 1 and
            count_numeros >= numeros_minimo and
            count_letras_maiuscula >= letras_maiusculas and
            count_letras_minusculas >= letras_minusculas
        ):
            return True
        else:
            return False




        
        
        
        
        
        
         