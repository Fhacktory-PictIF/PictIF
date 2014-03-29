#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from SimpleCV import Image

class I():
	"""Input mechanism"""
	def __init__(self):
		pass

	def read(self, path):
		# print "Reading ", path
		images = []
		if os.path.isfile(path):
			# print "Considering file ", path
			images.append(Image(path))
		elif os.path.isdir(path):
			# print "Considering directory ", path
			for dirname, dirnames, filenames in os.walk(path):
				for subdirname in dirnames:
					# print "Considering directory", subdirname
					images.append(self.read(subdirname))
				for filename in filenames:
					# print "Considering file ", filename
					img = Image(dirname+filename)
					img.show()
					images.append(img)
		return images

class O():
	"""Output mechanism"""
	def __init__(self):
		pass

	def write(self, lol):
		pass

class ImageData():
	"""Image object"""
	def __init__(self, arg):
		self.arg = arg
