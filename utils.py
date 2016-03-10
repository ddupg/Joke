# -*- coding: utf-8 -*-

import yaml
import os

def get_settings(path_settings=None):

	'''
		path_settings必须是文件的绝对路径

	'''

	if not os.path.isabs(path_settings):
		raise Exception('%s should be absoule path.' % path_settings)
	

	with open(path_settings, 'r') as fp:
		settings = yaml.load(fp)
		return settings

	return None
