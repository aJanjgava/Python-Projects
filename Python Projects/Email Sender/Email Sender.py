"""
    Email Sender
    Workflow:
        Go over to our gmail account and setup 2-step authentication
        Generate app password
        Create a function to the email
"""

from email.message import EmailMessage
from app_pass import password
import ssl
import smtplib

email_sender = 'pythontestfor@gmail.com'
email_password = password

email_reciever = ''  # email address goes here

subject = "Python Development"
body = """
    Python is a popular general-purpose programming language. 
    It is used in machine learning, web development, desktop applications, and many other fields. 
    Fortunately for beginners, Python has a simple, easy-to-use syntax. 
    This makes Python a great language to learn for beginners.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
