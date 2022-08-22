import smtplib
from email.message import EmailMessage
from string import Template

from emailatr import SMTPHOST, PASSWORD, ACCOUNT


def apmokek(kreipinys, elpastas, suma):
    with open('skola.html', mode='rt', encoding='utf-8') as f:
        html = f.read()

    sablonas = Template(html)

    email = EmailMessage()
    email['from'] = f"Atstovas. <{ACCOUNT}>"
    email['to'] = elpastas
    email['subject'] = 'Pranešimas apie permoką'

    email.set_content(sablonas.substitute({'kreipinys': kreipinys, 'permoka': suma}),
                      'html')

    with smtplib.SMTP(host=SMTPHOST, port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(ACCOUNT, PASSWORD)
        smtp.send_message(email)


apmokek('Ramūnai', 'destytojas@adomopython.smshostingas.lt', 250.25)
