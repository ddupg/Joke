# -*- coding: utf-8 -*-

from JokeGetter import JokeGetter
from MailSender import MailSender


if __name__ == '__main__':

	jokeGetter = JokeGetter()
	mailSender = MailSender()
	mailSender.send_mail(jokeGetter.get_jokelist())
	print('end of sending mail')
