from fastapi import FastAPI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


# Charger les variables d'environnement
load_dotenv()

# Récupérer les variables d'environnement
smtp_server = os.getenv("SMTP_SERVER")
port = int(os.getenv("SMTP_PORT"))
username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")
sender_email = os.getenv("SENDER_EMAIL")
to_email = os.getenv("TO_EMAIL")


app = FastAPI()

@app.get("/send")
def send_email():
    # Créer le message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = "Bienvenue !"

    html = """
        <html>
        <body>
            <h1>Salut !</h1>
            <p>Bienvenue dans notre application !</p>
        </body>
        </html>
    """
    part = MIMEText(html, "html")
    message.attach(part)
    
    try:
        # Configurer le serveur SMTP
        server = smtplib.SMTP(smtp_server, port)
        server.set_debuglevel(1)  # Activer le débogage pour voir les logs
        server.starttls()  # Activer le chiffrement TLS
        server.login(username, password)

        # Envoyer le message
        server.send_message(message)

        # Fermer la connexion
        server.quit()

        return {"message": "E-mail envoyé avec succès"}
    except Exception as e:
        return {"error": str(e)}
