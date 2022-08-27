# standartinis tekstinio emailo siuntimo kodas

import smtplib
from email.message import EmailMessage

from emailatr import SMTPHOST, PASSWORD, ACCOUNT

from_ = f"Ramunas P. <{ACCOUNT}>"
to = "destytojas@pythonkursas.smshostingas.lt"
subject = "Pirmasis Python email, Ramunas"

email_text = "Sveiki,\n tai yra laiško turinys"

email = EmailMessage()
email['from'] = from_
email['to'] = to
email['cc'] = to
email['subject'] = subject

email.set_content(email_text)

with smtplib.SMTP(host=SMTPHOST, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ACCOUNT, PASSWORD)
    smtp.send_message(email)
