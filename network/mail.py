import smtplib

sendfrom = "youdon'tknownwhoim"
sendtolist = ['havenyang@viatech.com.cn']

message = """hello, python email
this is the first mail sent by python
"""

try:
	smtp = smtplib.SMTP()
	smtp.connect("mailbj.viatech.com.cn")
	smtp.sendmail(sendfrom, sendtolist, message)
	smtp.close()
	print 'send email OK'
	
except:
	print 'Error: unable to send email'