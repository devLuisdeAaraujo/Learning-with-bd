import streamlit as st
from funcao_token import Conexao_token
from login import *
from time import sleep
class Email_token:
    def __init__(self):
        st.title("Verificação do e-mail")
        st.text('Em seu e-mail chegará um código de verificação com 6 (seis) dígitos.')
        value_put = st.text_input("Digite o código de verificação")
        
        #envia o codigo para o e-mail
        if 'validacao_code' not in st.session_state:
            token = Conexao_token()
            st.session_state.validacao_code = token.codigo
            token.send_email_objects()
            st.success('Código de verificação enviado para o e-mail!')

        

        #Caso voce queira reenviar seu codigo no email, mesma lógica
        if st.button('Reenviar código'):
            token = Conexao_token()
            st.session_state.validacao_code = token.codigo
            token.send_email_objects()
            st.success('Novo código enviado!')

        #validacao do botao
        if st.button('Validar', key='btn_token_email'):
            if value_put == '':
                st.warning('Nenhum código adicionado!')
            elif any(char.isalpha() for char in value_put):
                st.warning('O campo deve conter somente números!')
            elif value_put != st.session_state.validacao_code:
                st.warning(f'Código errado! Código esperado: {st.session_state.validacao_code}')  # Só pra debug
            else:
                st.success("E-mail verificado com sucesso! ")
                sleep(2.5)
                
if __name__ == "__main__":
    Email_token()
