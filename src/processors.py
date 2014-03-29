#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import Component
<<<<<<< HEAD
import numpy
from IO import I, O, ImageData
from SimpleCV import Color
=======
from IO import O
>>>>>>> 66aeed7580e0ecc915fb12f2a13b1a7b5bc5f47c

class Cropper(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.output = O()
		self.x = 0
		self.y = 0
		self.width = 100
		self.height = 100

	def process(self):

		img_input = self.input.readC(["../test/"])

		for im in img_input:
			im.image = im.image.crop(self.x,self.y,self.width,self.height)
		self.executed = True
		
		self.output.write(img_input,'../test/cropped/',self.name)

class GrayScale(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.output = O()
		self.degree = 1

	def process(self):
		img_input = self.input.readC(["../test/"])

		for im in img_input:
			(red, green, blue) = im.image.splitChannels(False)
			im.image = (red.toGray() + green.toGray() + blue.toGray()) / self.degree

		self.executed = True
		
		self.output.write(img_input,'../binarized/',self.name)

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
