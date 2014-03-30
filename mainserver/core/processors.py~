#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import Component
<<<<<<< HEAD
import numpy
from IO import O, ImageData
from SimpleCV import Color
=======
from SimpleCV import Color
from IO import O, ImageData
>>>>>>> 2dbc7bc999dc83689fb4a14176cd7cf3b85451ff

class Cropper(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.output = O()
		self.x = 0
		self.y = 0
		self.width = 100
		self.height = 100

	def process(self):

		for im in self.images:
			im.image = im.image.crop(self.x,self.y,self.width,self.height)
		
		self.output.write(self.images,'../cropped/',self.name)

		self.executed = True

class GrayScale(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.output = O()
		self.degree = 1

	def process(self):

		self.executeParent()
		
		for im in self.images:
			(red, green, blue) = im.image.splitChannels(False)
			im.image = (red.toGray() + green.toGray() + blue.toGray()) / self.degree

		self.executed = True
		
		self.output.write(self.images,'../binarized/',self.name)

class ChromaKey(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.green_screen = ImageData("../test/greenScreen.jpg")
		self.green_screen.load()
		self.background = ImageData("../test/landscape.jpg")
		self.background.load()
		self.green_screen.image = self.green_screen.image.scale(self.background.image.width, self.background.image.height)

	def process(self):
		mask = self.green_screen.image.hueDistance(color=Color.GREEN).binarize()
		import time
		
		result = (self.green_screen.image - mask) + (self.background.image - mask.invert())
		result.show()
		time.sleep(10)

if __name__ == "__main__" :

	import string
	suffixes = string.letters + string.digits
	binarizer = GrayScale(suffixes[0])
	suffixes = suffixes[1:]
	binarizer.process()
	chroma = ChromaKey(suffixes[0])
	suffixes = suffixes[1:]
	chroma.process()
