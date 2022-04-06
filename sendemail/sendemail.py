import smtplib
import ssl
from email.message import EmailMessage

# getting information regarding the sender and the message and the receiver
subject = "A Email from Akash"
body = "How are you ? "
sender_email = 'akashkukhe@gmail.com'
receiver_email = 'archnakhiwaliya@gmail.com'
password = input("enter your password: ")


# creating a new email
message = EmailMessage()
message["From"] = subject
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)


context = ssl.create_default_context()

# sending that email
print('Sending Email')
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print('success')
