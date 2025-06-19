# 📌 Sistema de Cadastro e Login com Validação de E-mail (Python + Streamlit + SQLite3)

Este projeto é uma aplicação web desenvolvida com **Python** e **Streamlit**, com objetivo de realizar **cadastro e login de usuários** com **verificação de e-mail**. Os dados são armazenados em um banco de dados **SQLite3**, com foco em segurança e validação.

---

##  Funcionalidades

- ✅ Cadastro de usuário (nome, CPF, e-mail e senha)
- ✅ Validação de e-mail com envio de código via **SMTP**
- ✅ Geração de token seguro com a biblioteca **secrets**
- ✅ Armazenamento de senha criptografada com **hashlib**
- ✅ Login permitido somente após validação do e-mail
- ✅ Login com nome, CPF,e-mail.

---

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- SQLite3
- smtplib (SMTP)
- secrets
- hashlib

---

## 💻 Como rodar o projeto localmente

**Pré-requisitos:**  
Python instalado na máquina e biblioteca Streamlit.

### Instalar o Streamlit:

```bash
pip install streamlit
```bash
streamlit run cadastre.py

