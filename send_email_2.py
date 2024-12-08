from email.message import EmailMessage
import os
import ssl
import smtplib

host = 'smtp.gmail.com'
port = 465

# Email details
email_sender = "lisawilson00222@gmail.com"
email_password = os.getenv("PASSWORD")
email_receiver = "onyemaechitasie@gmail.com"

subject = 'Sample Email'
# Email body
body = """
Hello,

This is a sample email.

Best regards,
Your Name
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as obj:
    obj.login(email_sender, email_password)
    obj.sendmail(email_sender, email_receiver, em.as_string())
