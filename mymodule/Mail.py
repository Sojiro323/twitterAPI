# coding: utf-8
#cording python3

def sendmail(text):

    import smtplib

    from email.mime.text import MIMEText
    from email.header import Header
    from email.utils import formatdate

    f = open('../../password/mail.yml', 'r+'):
    password = yaml.load(f)

    from_address = password["from_address"]
    to_address = password["to_address"]

    charset = 'ISO-2022-JP'
    subject = u'プログラムが完了しました'

    msg = MIMEText(text.encode(charset), 'plain', charset)
    msg['Subject'] = Header(subject, charset)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Date'] = formatdate(localtime=True)

    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(password["from_address"],password["p"])
    smtp.sendmail(from_address, to_address, msg.as_string())

    smtp.close()

    print("finish programming!!")
