from fastapi import FastAPI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


# Charger les variables d'environnement
load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("SMTP_PORT"))
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")
sender_email = os.getenv("SENDER_EMAIL")
to_email = os.getenv("TO_EMAIL")


app = FastAPI()


# Créer le message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = to_email
# message["Subject"] = "Bienvenue dans notre application !"


# Corps de l'e-mail
# text = f"Bonjour {to_email},\n\nBienvenue dans notre application ! Nous sommes ravis de vous compter parmi nous.\n\nCordialement,\nL'équipe."
# message.attach(MIMEText(text, "plain"))

@app.get("/send")
def send_email():

    html = """
        <html>
        <body>
            Salut
        </body>
        </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)

    server = smtplib.SMTP(smtp_server, port)
    server.set_debuglevel(1)
    server.esmtp_features["auth"] = 'LOGIN PLAIN'
    server.login(username, password)
    server.send_message(message)

    return {"Hello MTFCK"}