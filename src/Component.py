#!/usr/bin/env python
# -*- coding: utf-8 -*-
from IO import I, O

class Component():

    def __init__(self, name) :
    	self.name = name

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

class Croper(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.input = I("entry")
		self.output = O("output")

	def process():
		images = [i.crop(100,100,50,50)]
		return ''

def createComponent(names):
	comp = Component(names[0])
	return names[1:], comp

if __name__ == "__main__" :

	import string
	names = string.letters + string.digits
	print names

	names, component = createComponent(names)

	print names

	