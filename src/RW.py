#!/usr/bin/env python
# -*- coding: utf-8 -*-
from component import Component
from IO import O

class Reader(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.length = None
		self.key_points = []
		self.mean_colors = []

	def process(self, pathes):
		self.images = self.read(pathes)
		self.length = len(img_input)
		self.key_points = [i.image.findKeypoints() for i in img_input]
		self.mean_colors = [k.meanColor() for k in self.key_points]
		self.executed = True

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
		self.images = images

class Writer(Component):
	"""docstring for Writer"""
	def __init__(self, arg):
		Component.__init__(self, arg)
		self.arg = arg
		
	def process(path):
		O.write(self.images, path, "")
		self.executed = True