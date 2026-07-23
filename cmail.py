import smtplib
from email.message import EmailMessage
def send_mail(to,body,subject):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('aravindyadla6@gmail.com','jnik wzmu reiq iiah')
    msg=EmailMessage()
    msg['FROM']='aravindyadla6@gmail.com'
    msg['TO']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('mail sent')
    server.quit()
