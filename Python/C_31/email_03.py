#  čia panaudojam šabloną (Template), taip galim pakeisti
#  $vardas paėmę iš žodyno reikšmę pagal tokį raktą


import smtplib
from email.message import EmailMessage
from string import Template

from emailatr import SMTPHOST, PASSWORD, ACCOUNT

from_ = f"Ramunas P. <{ACCOUNT}>"
to = "destytojas@pythonkursas.smshostingas.lt"
subject = "Python HTML emailas panaudojant šabloną, Ramunas"

with open('sablonas.html', mode='rt', encoding='utf-8') as f:
    email_html_text = f.read()

sablonas = Template(email_html_text)

email = EmailMessage()
email['from'] = from_
email['to'] = to
email['cc'] = ACCOUNT
email['subject'] = subject

email.set_content(sablonas.substitute({'vardas': 'Kintamasis'}), 'html')

with smtplib.SMTP(host=SMTPHOST, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ACCOUNT, PASSWORD)
    smtp.send_message(email)
