from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from funcao_email_recente import pegar_linha_mais_recente, pegar_linha_mais_recente_cpf
import secrets

class Conexao_token:
    def __init__(self):
        #pegar o email from e colocar sua senha para acesso, a senha correta que voce pega no google AppSenha nada funciona
        self.email_from = 'luis.araujo.sesisenaisp@gmail.com'
        self.password = 'vidv cjem zbzh mrmx'
        self.email_smtp_server = 'smtp.gmail.com'
        self.email_destino = pegar_linha_mais_recente()
        self.cpf_destino = pegar_linha_mais_recente_cpf()
        self.codigo = self.code_send()
        #mensagem no terminal enviando email para {Gusta@gmail.com}
        if self.email_destino:
            self.destination = [self.email_destino]
            print(f"Enviando e-mail para {self.destination}")
        else:
            self.destination = []
            print('Nenhum e-mail detectado')
        #Aqui eu to usando o secrets e to salvando ele no state
    def code_send(self):
        self.codigo = str(secrets.randbelow(900000) + 100000)  # Gera código como string de 6 dígitos
        return self.codigo


    def send_email_objects(self):
        if not self.destination:
            print("Nenhum destinatário para enviar o e-mail.")
            return
        #caso nao tenha escrito nada dentro do input

        msg = MIMEMultipart()
        msg['From'] = self.email_from
        msg['To'] = ', '.join(self.destination)
        msg['Subject'] = 'Verificação do e-mail'
        #A biblioteca Mime usada para fazer a configuração de email enviado

        corpo = f"""
        <html>
            <body>
                <p>Olá, um novo cadastro com o CPF {self.cpf_destino} foi realizado.</p>
                <p>Por favor valide o cadastro. Seu código é: <strong>{self.codigo}</strong></p>
            </body>
        </html>
        """ #Corpo da mensagem a ser enviada

        msg.attach(MIMEText(corpo, 'html'))
            #usada para add a mensagem , no corpo do email
        try:
            with smtplib.SMTP(self.email_smtp_server, 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(self.email_from, self.password)
                smtp.sendmail(self.email_from, self.destination, msg.as_string())
            print(f"E-mail enviado com sucesso com o código: {self.codigo}")
        except Exception as erro:
            print(f'Erro ao enviar o e-mail de verificação: {erro}')
                #aqui que o email será enviado

if __name__ == "__main__":
    token = Conexao_token()
    token.send_email_objects()
