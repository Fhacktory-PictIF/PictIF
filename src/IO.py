#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ntpath
from SimpleCV import Image

class I():
	"""Input mechanism"""
	def __init__(self):
		pass

	def read(self, pathes):
		# print "Reading ", path
		for path in pathes:
			# print "Considering path ", path 
			images = []
			if os.path.isfile(path):
				# print "Considering file ", path
				images.append(ImageData(path))
			elif os.path.isdir(path):
				# print "Considering directory ", path
				for dirname, dirnames, filenames in os.walk(path):
					for subdirname in dirnames:
						# print "Considering directory", subdirname
						images += self.read(subdirname)
					for filename in filenames:
						# print "Considering file ", filename
						img = ImageData(os.path.join(dirname, filename))
						images.append(img)
		return images

	def readC(self, path):
		images = self.read(path)
		for image in images:
			image.load()
		return images

class O():
	"""Output mechanism"""
	def __init__(self):
		pass

	def write(self, images, path, ComponentId):
		for image in images:
			write(image, path)

	def write(self, image, path, ComponentId):
		image.save(path + image.name + ComponentId + image.extension)
		pass

class ImageData():
	"""Image object"""
	def __init__(self, path):
		self.path = path
		self.name = os.path.splitext(os.path.basename(path))[0]
		self.extension = os.path.splitext(path)[1]
		self.image = None
		self.suffixes = ""

	def load(self):
		self.image = Image(self.path)

	def unload(self):
		del self.image
