import smtplib, ssl

host = "smtp.gmail.com"
port = 465

email = "lisawilson00222@gmail.com"
password = "xabjoyncavfgthto"
receiver = "onyemaechitasie@gmail.com"

my_context = ssl.create_default_context()

message = """\
Subject: Email from Python
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(email, password)
    server.sendmail(email, receiver, message)