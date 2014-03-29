#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SimpleCV import Image
from io import I, O

class Component():

    def __init__(self, name) :
    	self.name = name
    	self.executed = False

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

class Cropper(Component):

	def __init__(self, name, x, y, width, height):
		Component.__init__(self, name)
		self.input = I("entry")
		self.output = O("output")
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def process(self):
		#TODO : replace with I.read()
		img_input = []
		for i in range(1,5):
			img = Image("../test/img" + str(i) + ".jpeg")
			img_input.append(img)

		images = [i.crop(self.x,self.y,self.width,self.height) for i in img_input]
		self.executed = True
		#TODO : replace with O.write()
		for i,k in zip(images,range(1,5)):
			i.save("../test/imgT" + str(k) + ".jpeg")

def createComponent(names):
	comp = Component(names[0])
	return names[1:], comp

if __name__ == "__main__" :

	import string
	names = string.letters + string.digits

	names, component = createComponent(names)
	cropper = Cropper(names[0],100,100,50,50)
	cropper.process()

	