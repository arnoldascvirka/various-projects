# čia siunčiame html tekstą iš failo index.html

import smtplib
from email.message import EmailMessage

from emailatr import SMTPHOST, PASSWORD, ACCOUNT

from_ = f"Ramunas P. <{ACCOUNT}>"
to = "destytojas@pythonkursas.smshostingas.lt"
subject = "Pirmasis Python HTML emailas, Ramunas"

with open('index.html', mode='rt') as f:  # nuskaitomas failas
    email_html_text = f.read()

email = EmailMessage()
email['from'] = from_
email['to'] = to
email['cc'] = ACCOUNT
email['subject'] = subject

email.set_content(email_html_text, 'html')  # nurodome .set_content email formatą 'html'

with smtplib.SMTP(host=SMTPHOST, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ACCOUNT, PASSWORD)
    smtp.send_message(email)
