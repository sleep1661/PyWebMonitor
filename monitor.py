#coding: utf-8
import watchweb
import os
import smtplib
import re
from email.mime.text import MIMEText
from email.header import Header
import urllib
from apscheduler.schedulers.gevent import GeventScheduler
import logging
#shutdown ssl verify
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def send_mail(web):
	sender = os.environ['WM_MAIL_SENDER']
	receiver = web[watchweb.MAIL_RECEIVER]
	subject = web[watchweb.MAIL_MSG]
	smtpserver = os.environ['WM_MAIL_SMTPSERVER']
	username = os.environ['WM_MAIL_USERNAME']
	password = os.environ['WM_MAIL_PASSWORD']
	msg = MIMEText('<html><h1>%s</h1></html>'% subject,'html','utf-8') 
	msg['Subject'] = Header(subject, 'utf-8')

	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()


def check_web(**web):
	data = urllib.urlopen(web[watchweb.URL]).read()
	r = re.compile(web[watchweb.REGEX].encode('utf-8'))
	infos = r.findall(data)
	for info in infos:
		if eval(web[watchweb.CONDITION]):
			print 'send mail...'
			send_mail(web)


def watch():
	scheduler = GeventScheduler()
	
	for web in watchweb.get_watch_webs():
		s = int(web[watchweb.INTERVAL_SECONDS])
		scheduler.add_job(check_web, 'interval', seconds=s,kwargs=web)


	g = scheduler.start()  # g is the greenlet that runs the scheduler loop
	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

	# Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
	try:
		g.join()
	except (KeyboardInterrupt, SystemExit):
		pass

		
if __name__ == '__main__':
	logging.basicConfig(filename = 'monitor.log',level=logging.ERROR)
	watch()
		