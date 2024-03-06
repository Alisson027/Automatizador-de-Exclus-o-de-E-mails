# Automatizador de Exclusao de E-mails
Este repositório abriga um script em Python desenvolvido para facilitar o processo de exclusão de e-mails em contas do Gmail. Utilizando a biblioteca imaplib, o script conecta-se de forma segura ao servidor IMAP do Gmail, busca por e-mails que atendem a critérios específicos (assunto "PicPay" ou texto "picpay") e os exclui permanentemente.

Funcionalidades

    Conexão segura ao servidor IMAP do Gmail.
    Busca por e-mails com o assunto "PicPay" ou contendo o texto "picpay".
    Obs: O texto pode ser alterado por  um de seu interesse. 
    Exclusão permanente dos e-mails encontrados.

# Como Usar

    Clone o repositório para o seu ambiente local.
    Configure as informações da sua conta do Gmail no script.
    Execute o script para automatizar a exclusão de e-mails.

# Pré-requisitos

    Python instalado.
    Bibliotecas necessárias instaladas (imaplib, email).

bash

pip install imaplib
pip install email

Lembre-se de testar cuidadosamente antes de usar em um ambiente de produção.

# Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou propor melhorias no código.

Espero que este script seja útil para simplificar o gerenciamento de e-mails no Gmail.

