import smtplib
sender_mail = 'ashwinimwerulkar@gmail.com'
receiver_mail = 'ashwinimwerulkar@gmail.com'
message = """From: From person %s To: To person %s Subject: Sending SMTP Email This is a test mail"""%(sender_mail,receiver_mail)
try:
    password= input('Enter the password')
    smtpObj = smtplib.SMTP('gmail.com', 587)
    smtpObj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail,receiver_mail,message)
    print("Success")
except Exception:
    print("Failed")