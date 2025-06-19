# Sistema de Cadastro e Login com Validação de E-mail (Python + Streamlit + SQLite3)

Este projeto é uma aplicação web desenvolvida com **Python** e **Streamlit**, com objetivo de realizar **cadastro e login de usuários** com **verificação de e-mail**. Os dados são armazenados em um banco de dados **SQLite3**, com foco em segurança e validação.

---

##  Funcionalidades

- Cadastro de usuário (nome, CPF, e-mail e senha) *CPF precisa ser verídico.*
- Validação de e-mail com envio de código via **SMTP**
- Geração de token seguro com a biblioteca **secrets**
- Armazenamento de senha criptografada com **hashlib**
- Login permitido somente após validação do e-mail
- Login com nome, CPF,e-mail.

---

##  Tecnologias utilizadas

- Python
- Streamlit
- SQLite3
- smtplib (SMTP)
- secrets
- hashlib

---

## Como rodar o projeto localmente

**Pré-requisitos:**  
Python instalado na máquina e biblioteca Streamlit.
## **Estrutura dos arquivos principais:**
 - cadastre.py -> Tela de cadastro de usuários.
 - login.py -> Tela de login dos usuários
 - funcao_token.py -> Geração de código/ token de verificação.
 - token_email.py -> Envio de e-mail com o código via **SMTP**
 - funcao_email_recente.py -> Verificação do código/ token enviado
 - cadastre_user.db -> Banco de dados **SQLITE3** (gerado automaticamente ao rodar)
 - 

### Instalar o Streamlit:

```bash
pip install streamlit
```

## -PASSO 1: Fazendo a aplicação web:
```bash
streamlit run cadastre.py
```
Neste tela você conseguirá fazer o cadastro na página: Cadastrando seu nome de usuário, seu e-mail o qual vai receber o código , seu cpf *Precisa ser cpf verídico*, sua senha *Senha vai ser criptografada dentro do banco de dados utilizando a biblioteca hashlib*. Após isso cadastrá-lo clicando no botão.

## -PASSO 2: Redirecionamento para verificação e-mail:

Você será redirecionado automáticamente para a página de validação, o qual vai ser enviado um e-mail no própio cadastrado, após isso faça a verificação de acordo com o código enviado.*CÓDIGO NÃO É VALIDADO PELO BANCO DE DADOS* Preferi utilizando nessa versão , apenas pelo metódo.
Podendo pedir o reenviamento desse código, o qual será diferente.

## -PASSO 3: Realizando login:
Após a validação você pode fechar o web já aberto no seu terminal e reabrir usando
```bash
streamlit run login.py
```
Nele fará o login com NOME ou E-MAIL ou CPF,  já cadastrado no Banco de dados, juntamente com sua senha cadastrada.

Caso errar em algo aparecerá a tela.
Se realizar o login corretamente, aparecerá **login concluído com sucesso**.

## -Observações:

-O envio de e-mails está configurado inicialmente para Gmail, mas pode ser adaptado para outros servidores.
-As senhas são **criptografadas** antes de serem armazenadas, aumentando a segurança do sistema.
-Caso queira testar com outro e-mail, é necessário alterar as configurações de **SMTP** no código.

## -Contate-me:

**E-mail**
```bash
E-mail: luis.araujo.sesisenaisp@gmail.com
````
**Telefone**
```bash
+55 (11) 97470-0738
```
**Instagram**
```bash
@l.gustazz
```







