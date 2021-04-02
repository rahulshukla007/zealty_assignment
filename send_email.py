# Assignment 1:
# Write a python class that is able to send an email from the terminal to a given email address
# using smtplib library.



#Before running this code please fill your email
#inside the sender_mail & password otherwise it will not work

#Allow less secure apps: ON in case if your credentials not work
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
#please use your own email & password
sender_email   = '' 
sender_password = ''

msg['From']     = sender_email
Body            = input('please give email body ')   
msg['Subject']  = input('please enter the subject ')   
msg['To']       = input('please enter the email address of the recipient ') 
msg.set_content(Body)

if sender_email != '' and sender_password != '':
    try:    
        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()  
        print("Email sent!")    
    except Exception as e:    
        print(e)  
else:
    print('Unable to send email ------> please set sender email & password first <-------- warning')

