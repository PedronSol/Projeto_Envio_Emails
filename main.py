import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def hello_world():
    print("Hello World!")
# Configurações do servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'  # Altere para o servidor SMTP que você vai usar
SMTP_PORT = 587  # Porta para TLS
USERNAME = 'NAORESPONDER@HOSPITALRIOGRANDE.com.br'  # Seu e-mail
PASSWORD = 'hr@G1#4aH'  # Sua senha

schedule.every(10).seconds.do(hello_world)
# Configurando o conteúdo do e-mail
remetente = USERNAME
destinatario = 'testehrg20@gmail.com'  # E-mail do destinatário
assunto = 'Controle de Pendências - Hospital Rio Grande'
corpo = '''<table style="width: 95%; margin-left: 2.5%; background-color: #eee;">
  <thead>
    <tr>
      <td>
        <img style="margin-top: 10px; margin-left: 10px;" src="https://www.hospitalriogrande.com.br/assets/site/images/logo-hospital-rio-grande.png" alt="Logo do Hospital Rio Grande com texto" width="300px">
        <h1 style="margin: 20px 0; padding-left: 10px; text-align: center;">Meus textos no Medium</h1>
      </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <img style="margin-left: 10px; margin: 20px 0;" src="https://miro.medium.com/fit/c/112/112/0*mMNSf7T5NMC9X_Hb" alt="code" align="right">
        <h2 style="color: #163045; padding-left: 10px; margin-top: 20px;">Texto 1</h2>
        <p style="font-size: 18px; color: #163045; margin-bottom: 5px; padding-left: 10px;">Testes unitários: O que saber antes de iniciar, 6 dicas</p>
        <a href="https://jvvoliveira.medium.com/testes-unit%C3%A1rios-o-que-saber-antes-de-iniciar-6-dicas-d00319e3ca5b" target="_blank" rel="noopener noreferrer" style="color: #292; cursor: pointer; padding-left: 10px;">ler</a>
      </td>
    </tr>
  </tbody>
</table>'''

def enviar_emails(mensagem_padrao, mensagem_html):
    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem_padrao, 'plain'))
    msg.attach(MIMEText(mensagem_html, 'html'))

    try:
        # Conexão com o servidor SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Inicia a criptografia TLS
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
            print(f'E-mail enviado para {destinatario}')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

schedule.every(10).hours.do(enviar_emails)

while True:
    schedule.run_pending()