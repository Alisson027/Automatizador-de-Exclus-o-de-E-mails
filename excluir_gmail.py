import imaplib
import email
from email.header import decode_header

# Configurações do e-mail
email_user = # coloque o  seu email
email_pass = #coloque a sua senha de app do Gmail.

# Conectar-se ao servidor IMAP usando imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Fazer login na conta
mail.login(email_user, email_pass)

# Selecionar a caixa de entrada (inbox)
mail.select('inbox')

# Buscar todos os e-mails que contenham o assunto"PicPay" ou corpo
status, messages = mail.search(None, '(OR SUBJECT "PicPay" TEXT "picpay")')

if status == 'OK':
    email_ids = messages[0].split()
    if not email_ids:
        print("Nenhum e-mail encontrado com o termo 'Testes'.")
    else:
        # Excluir os e-mails
        for email_id in email_ids:
            mail.store(email_id, '+FLAGS', '(\Deleted)')

        #excluir os e-mails marcados para exclusão
        #O expunge exlcui definitivamente, nao manda para a lixeira
        mail.expunge()
        print("E-mails contendo 'teste' excluídos com sucesso.")

# sair
mail.logout()










