# coding: utf-8
#cording python3

def sendmail(text):

    import smtplib

    from email.mime.text import MIMEText
    from email.header import Header
    from email.utils import formatdate

    from_address = 'm23622059@gmail.com'
    to_address = 'm23622059@i.softbank.jp'

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
    smtp.login('m23622059@gmail.com','m23622059')
    smtp.sendmail(from_address, to_address, msg.as_string())

    smtp.close()

    print("finish programming!!")
