from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_email = "YOUR EMAIL HERE"
    from_passwrod = "YOUR PASSWORD HERE"
    to_email = email

    subject = "Height Data!"
    message = "Hey there, your height is <b>%s</b> <br>The height average is <b>%s</b> (average of <b>%s</b> heights)" % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    # SMTP CONFIG HERE
    gmail = smtplib.SMTP('smtp.gmail.com', 587) 
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_passwrod)
    gmail.send_message(msg)
