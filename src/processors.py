#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import Component
from IO import I, O

class Cropper(Component):

	def __init__(self, name, x, y, width, height):
		Component.__init__(self, name)
		self.input = I()
		self.output = O()
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def process(self):

		img_input = self.input.readC(["../test/"])

		images = [i.image.crop(self.x,self.y,self.width,self.height) for i in img_input]
		self.executed = True
		#TODO : replace with O.write()
		for i,k in zip(images,range(4)):
			i.save("../test/temp/imgT" + str(k) + ".jpeg")
			img_input[k].unload()

class Binarizer(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.input = I()
		self.output = O()

	def process(self):
		#TODO : replace with I.read()
		img_input = self.input.read("../test/")

		images = [i.image.binarize() for i in img_input]
		self.executed = True
		#TODO : replace with O.write()
		for i,k in zip(images,range(4)):
			i.save("../test/imgT" + str(k) + ".jpeg")
			img_input[k].unload()