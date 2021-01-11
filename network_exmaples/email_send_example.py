import smtplib
import ssl

port = 587  # For SSL
smtp_server = "mail.4tester.net"
sender_email = "regev@4tester.net"  # Enter your address
receiver_email = "alex@vaiolabs.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
password="Cyber123456!"
message = """
Subject: Hi there

This message is sent from Python as test.
"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
