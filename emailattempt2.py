import smtplib
def sendEmail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	#Next, log in to the server
	server.login("email", "pass")
	
	#Send the mail
	msg = "Hello!" # The /n separates the message from the headers
	server.sendmail("jake.happersett@gmail.com", "8042100901@msg.fi.google.com", msg) 

sendEmail()
