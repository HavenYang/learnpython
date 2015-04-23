import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sendfrom = 'havenyang@viatech.com.cn'
sendtolist = 'havenyang@viatech.com.cn;havenyang@126.com'
attachlist = ['mail.py', '123.txt']

message = """
hello python mail.
this is the first mail sent by python.
this step, have defined functions
"""

def constructure_message(sender, recvlist, subject, bodymsg):
	msg = MIMEMultipart()
	
	msg['from'] = sender
	msg['to'] = recvlist
	msg['subject'] = subject
	
	att = MIMEText(message, 'base64', 'gb2312')
	att['Content-Type'] = 'text'
	
	msg.attach(att)
	return msg

def msg_add_attach(msg, attfilename):
	att = MIMEText(open(attfilename,'rb').read(), 'base64', 'gb2312')
	att['Content-Type'] = 'application/octet-stream'
	att['Content-Disposition'] = 'attachment; filename = ' + attfilename
	msg.attach(att)
	
def send(msg):
	try:
		smtp = smtplib.SMTP()
		smtp.connect("mailbj.viatech.com.cn")
		#login by username and password here
		#smtp.login(username, password)
		smtp.sendmail(msg['from'], msg['to'], msg.as_string())
		smtp.close()
		print 'send email OK'
	except:
		print 'Error: unable to send email'
	
def send_mail(sender, recvlist, subject, bodymsg):
	msg = constructure_message(sender, recvlist, subject, bodymsg)
	send(msg)
	
def send_mail_withattach(sender, recvlist, subject, bodymsg, attlist):
	msg = constructure_message(sender, recvlist, subject, bodymsg)
	
	for eachatt in attlist:
		msg_add_attach(msg, eachatt)
		
	send(msg)

def main():
	send_mail(sendfrom, sendtolist, 'functions', message)
	send_mail_withattach(sendfrom, sendtolist, 'functions with attach', message, attachlist)

main()