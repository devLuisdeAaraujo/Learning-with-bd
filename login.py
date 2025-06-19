import streamlit as st
import sqlite3
import hashlib
class LoginConnect:
    def __init__(self):
        st.text('Login')
        self.user_input = st.text_input('Usuário')
        self.password_login = st.text_input('Senha',type='password')
        self.button_login= st.button('Logar',key='button_login')
        

        #Se o botao for acionado
        if self.button_login:
            if self.user_input == '' or self.password_login == '':
                st.warning("Por favor, preencha todos os campos.")
            else:
                if self.verificar_login(self.user_input, self.password_login):
                    st.success('Login feito com sucesso!')
                else:
                    st.error('Usuário ou senha incorretos.')

        
    #verificação dos usuarios e senha puxando pelo banco de dados
    def verificar_login(self,user_input,senha_digitada):
        conexao = sqlite3.connect("cadastre_user.db")
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT senha FROM usuarios
            WHERE nome = ? OR cpf = ? OR email = ?
        """, (user_input, user_input, user_input))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            senha_no_banco = resultado[0]  
            senha_digitada_criptografada = self.senha_criptografada(senha_digitada)

            
            return senha_digitada_criptografada == senha_no_banco
        else:
            return False
        #senha criptografada usando hashlib como biblioteca
    def senha_criptografada(self,senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    


if __name__ == "__main__":
    LoginConnect()