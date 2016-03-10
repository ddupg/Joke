# -*- coding: utf-8 -*-

import os
import json
import sys
import urllib, urllib2
import requests

from utils import get_settings


class JokeGetter(object):
	def __init__(self):

		self.dir_name = os.path.dirname(os.path.abspath((__file__)))
		self.filename = os.path.join(self.dir_name, 'settings.yaml')
		self.settings = get_settings(self.filename)

		self.url = self.settings['API']['URL']
		self.apikey = self.settings['API']['APIKEY']
		

	def get_jokelist(self):

		req = urllib2.Request(self.url)
		req.add_header("apikey", self.apikey)
		resq = urllib2.urlopen(req)
		content = resq.read()
		if(content):
			contentlist = json.loads(content)['showapi_res_body']['contentlist']
			jokelist = [(x['title'], x['text']) for x in contentlist]
			return jokelist
