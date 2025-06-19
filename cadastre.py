import streamlit as st
from dados import Conectar
from dados import *
import funcao_token
from time import sleep
from token_email import Email_token
class CadastreUser:
    def __init__(self):
        st.title('Cadastro de usuário:')

        self.nome = st.text_input('Nome de usuário:')
        self.cpf = st.text_input('CPF:') 
        self.email = st.text_input('Seu e-mail:')
        self.senha = st.text_input('Sua senha:', type='password')
        
        

        if st.button('Enviar', key='cadastre_button'):

            if not Conectar.validar_cpf(self.cpf):
                st.warning('Usuário com cpf inválido!')
            elif not Conectar.validate_email(self.email):
                st.warning("Usuário com e-mail inválido!")
            elif db.email_existe(self.email):
                st.warning('E-mail já cadastrado!')
            elif db.cpf_existe(self.cpf):
                st.warning('CPF já cadastrado!')
            elif not Conectar.verificar_senha(self.senha):
                st.warning('Senha deve ter no mínimo 8 caracteres, com pelo menos: 1 maiúscula, 1 minúscula, 1 número e 1 caractere especial.')
            else:
                
                senha_cripto = db.senha_criptografada(self.senha)
                db.insert_data(self.nome, self.cpf, self.email, senha_cripto)
                token = funcao_token.Conexao_token()
    
                st.success("Usuário cadastrado com sucesso!")
                sleep(2.5)
                
                


    
    

if __name__ == '__main__':  
    db= Conectar()
    db.create_table()
    CadastreUser()
