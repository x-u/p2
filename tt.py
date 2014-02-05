import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.uk.xensource.com')
s.set_debuglevel(1)
msg = MIMEText("""body""")
sender = 'me@example.com'
recipients = ['lei.xu2@gmail.com']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())