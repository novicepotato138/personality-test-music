import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

def sendEmail(time_msg, input_id, attachmentmsg):
    # x = datetime.datetime.now()
    # time_msg = x.strftime("%c")
    # attachmentmsg = time.strftime('%x-%X')

    mail_content = '''Attachment indicates new submission from the questionnaire site as following timing: ''' + time_msg

    #The mail addresses and password
    sender_address = 'bananaate12138@gmail.com'
    sender_pass = 'hmkskggnsyogrcxp'
    receiver_address = 'jessywoon@gmail.com'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = "[Questionnaire entry] " + time_msg

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'X1.csv'

    payload=MIMEApplication(open(attach_file_name,"rb").read())

    encoders.encode_base64(payload)


    # Add header to variable with attachment file
    payload.add_header('Content-Disposition', 'attachment', filename= 'entry-' + attachmentmsg + '.csv')
    # Then attach to message attachment file    
    message.attach(payload)


    # Error Handling
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.ehlo()
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    except: 
        print('Mail Not Sent')
