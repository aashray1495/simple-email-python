import smtplib, ssl

smtp_server='smtp.gmail.com'
port=465
#port=587 for starttls for upgrading unencrypted to encrypted

sender='nubee@gmail.com'

password=input('Enter your password: ')

receiver= 'FAANG@gmail.com'
message="""\
From: {}
To: {}
Subject: What's up?

This is a new message""".format(sender,receiver)

ssl_context=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=ssl_context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print('It worked')
