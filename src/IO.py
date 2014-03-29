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

class ImageData():
	"""Image object"""
	def __init__(self, path):
		self.path = path
		self.image = None
		self.suffixes = ""

	def load(self):
		self.image = Image(self.path)

	def unload(self):
		del self.image
