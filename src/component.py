#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Component():

    def __init__(self, name) :
    	self.parent = None
    	self.name = name
    	self.images = None
    	self.executed = False

    def setParent(parent):
    	self.parent = parent
    	if parent is None :
    		self.executed = False

    def isSafelyExecuted():
    	return False if (self.parent is None) else True if isinstance(self.parent, Reader) and self.parent.executed else self.parent.isSafelyExecuted()

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

def createComponent(names):
	comp = Component(names[0])
	return names[1:], comp

if __name__ == "__main__" :

	import string
	names = string.letters + string.digits

	names, component = createComponent(names)
	#cropper = Cropper(names[0],100,100,50,50)
	#cropper.process()