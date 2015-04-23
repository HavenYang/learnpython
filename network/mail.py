import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sendfrom = "havenyang@viatech.com.cn"
sendtolist = ['havenyang@viatech.com.cn']

message = """
hello python mail 
this is the first mail sent by python.
"""

#create a instance with attachment
msg = MIMEMultipart()

#constructure a attachment
att1 = MIMEText(open('mail.py','rb').read(), 'base64', 'gb2312')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename = "123.txt"'
msg.attach(att1)

msg.set_payload(message)

msg['subject'] = 'dingdong'

try:
	smtp = smtplib.SMTP()
	smtp.connect("mailbj.viatech.com.cn")
	smtp.sendmail(sendfrom, sendtolist, msg.as_string())
	smtp.close()
	print 'send email OK'
	
except:
	print 'Error: unable to send email'