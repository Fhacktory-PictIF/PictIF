#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SimpleCV import Image
import os

class I():
	"""Input mechanism"""
	def __init__(self):
		pass

	def read(self, oseflol):
		images = []
		print "Reading ", oseflol
		for dirname, dirnames, filenames in os.walk(oseflol):
			for subdirname in dirnames:
				print "Considering directory", subdirname
				images.append(self.read(subdirname))
			for filename in filenames:
				print "Considering file ", filename
				img = Image(dirname+filename)
				img.show()
				images.append(img)
		return images

class O():
	"""Output mechanism"""
	def __init__(self, arg):
		self.arg = arg

