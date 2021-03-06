
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from tts import speak

speech_flag = True


def send_email(candid, attach_photo_flag):
    attachment = './captured_images/candidate_{0}.jpg'.format(candid)

    toemail = 'exitir@gmail.com'
    fromemail = 'mybotf5@gmail.com'
    msg = MIMEMultipart()
    # msg["To"] = 'exitir@gmail.com'
    # msg["From"] = 'mybotf5@gmail.com'
    msg["Subject"] = 'Candidate has arrived for interview.'
    body = "Below candiate : {0} has arrived for interview <hr>".format(candid)

    msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' %
                       (body, attachment), 'html')
    msg.attach(msgText)   # Added, and edited the previous line

    # print(msg)

    fp = open(attachment, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))

    msg.attach(img)

    # Gmail Sign In
    gmail_sender = 'mybotf5@gmail.com'
    gmail_passwd = 'mybot@123'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    # print(msg.as_string())

    try:
        server.sendmail('mybotf5@gmail.com',
                        'exitir@gmail.com', msg.as_string())
        print('email has been sent successfully')
        speak('email has been sent successfully', speech_flag)
    except:
        print('there was some error sending mail')
        speak('there was some error sending mail', speech_flag)

    server.quit()
