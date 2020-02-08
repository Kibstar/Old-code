import smtplib, os
myEmail = os.environ.get('GMAIL') ## Email and password are stored on the computers enviroment variables.
myPass = os.environ.get('PYTHON_GMAIL_PASS')

conn = smtplib.SMTP('smtp.gmail.com',587) ## Connects to the SMTP of the email host
conn.ehlo()  ## Starts the connection with email provider
conn.starttls() ## Starts encryption for password
conn.login(myEmail,myPass) ## Your login details for the email address you want to send from.
conn.sendmail(myEmail, myEmail,'Subject: Hello!\n\nHello! I am a Python script!\n\nPython') ## Main body of the email you want to send.
conn.close() ## Closes the connetion to the email host

