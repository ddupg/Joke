# -*- coding: utf-8 -*-

import os, sys

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

from utils import get_settings

class MailSender(object):

	def __init__(self):
		
		self.dir_name = os.path.dirname(os.path.abspath(__file__))
		self.filename = os.path.join(self.dir_name, 'settings.yaml')

		self.settings = get_settings(self.filename)

		self.from_addr = self.settings['MAIL']['FROM_ADDR']
		self.password = self.settings['MAIL']['PASSWORD']
		self.to_addr = self.settings['MAIL']['TO_ADDR']

		self.smtp_server = self.settings['MAIL']['SMTP_SERVER_ADDR']
		self.port = self.settings['MAIL']['SMTP_SERVER_PORT']

	
	def _format_addr(self, s):
		name, addr = parseaddr(s)
		return formataddr((Header(name, 'utf-8').encode(), addr))


	def send_mail(self, jokelist):
		msg = MIMEText(self._jokelist_to_string(jokelist), 'plain', 'utf-8')
		msg['From'] = self._format_addr('发件人 <%s>' % self.from_addr)
		msg['To'] = self._format_addr('收件人 <%s>' % self.to_addr)
		msg['Subject'] = Header('天天有笑话', 'utf-8').encode()

		server = smtplib.SMTP(self.smtp_server, self.port)
		server.login(self.from_addr, self.password)
		server.sendmail(self.from_addr, self.to_addr, msg.as_string())
		server.quit()

	
	def _jokelist_to_string(self, jokelist):
		
		joke = ''
		for title, text in jokelist:
			
			joke += title + '\n'
			joke += text + '\n'	
			joke += '-' * 50
			joke += '\n' * 2
		return joke
