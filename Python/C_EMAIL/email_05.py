import smtplib
from email.message import EmailMessage
from string import Template
import mimetypes

from emailatr import SMTPHOST, PASSWORD, ACCOUNT

from_ = f"Ramunas P. <{ACCOUNT}>"
to = "destytojas@adomopython.smshostingas.lt"
subject = "Python HTML emailas su keletu prisegtuku"

with open("sablonas.html", mode="rt", encoding="utf-8") as f:
    email_html_text = f.read()

sablonas = Template(email_html_text)

email = EmailMessage()
email["from"] = from_
email["to"] = to
email["cc"] = ACCOUNT
email["subject"] = subject

email.set_content(sablonas.substitute({"vardas": "Kintamasis"}), "html")

files = ['fox-gradient.png', '1200px-Sunflower_from_Silesia2.jpg']

for file in files:
    mimetype = mimetypes.guess_type(file)[0]
    subtype = mimetype.split('/')[1]
    with open(file, 'rb') as f:
        content = f.read()
        email.add_attachment(
            content,
            maintype=mimetype,
            subtype=subtype,
            filename=file
        )

with smtplib.SMTP(host=SMTPHOST, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ACCOUNT, PASSWORD)
    smtp.send_message(email)


