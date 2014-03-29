#!/usr/bin/env python
# -*- coding: utf-8 -*-

from RW import Reader
class Component():

    def __init__(self, name) :
    	self.parent = None
    	self.name = name
    	self.images = None
    	self.executed = False

    def setParent(self,parent):
    	self.parent = parent
    	if parent is None :
    		self.executed = False

    def isSafelyExecuted(self):
    	return False if (self.parent is None) else True if isinstance(self.parent, Reader) and self.parent.executed else self.parent.isSafelyExecuted()

    def executeParent(self):
    	if not self.parent.executed:
    		self.parent.process()

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

if __name__ == "__main__" :

	pass
