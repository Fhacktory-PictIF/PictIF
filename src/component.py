#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IO import I, O, ImageData

class Component():

    def __init__(self, name) :
    	self.name = name
    	self.executed = False

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

class Reader(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.input = I()
		self.output = O()
		self.length = None
		self.key_points = []
		self.mean_colors = []

	def process(self):
		#TODO : replace with I.read()
		img_input = self.input.read("../test/")

		self.length = len(img_input)
		self.key_points = [i.image.findKeypoints() for i in img_input]
		self.mean_colors = [k.meanColor() for k in self.key_points]
		self.executed = True

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

def createComponent(names):
	comp = Component(names[0])
	return names[1:], comp

if __name__ == "__main__" :

	import string
	names = string.letters + string.digits

	names, component = createComponent(names)
	cropper = Cropper(names[0],100,100,50,50)
	cropper.process()