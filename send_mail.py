import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_email = "lisawilson00222@gmail.com"
    password = "xabjoyncavfgthto"
    receiver = "onyemaechitasie@gmail.com"

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)