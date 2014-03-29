#!/usr/bin/env python
# -*- coding: utf-8 -*-

from RW import Reader

class Component():
    ioComponents = dict(Reader='Picture Reader', Writer='Picture Writer')
    processors = dict(Cropper='Cropper', GrayScale='Gray Scale', ChromaKey='Chromakey')
    selectors = dict(RowFilter='File Filter', Joiner='Joiner', Splitter='Splitter')
    statistics = []
    #classmere.__subclasses__() return list

    components = dict(ioComponents='I/O', processors='Processors', selectors='Selectors', statistics='Statistics')

    def __init__(self, name) :
    	self.parent = None
    	self.name = name
    	self.images = None
    	self.executed = False
        self.description = ""

    def setParent(self,parent):
    	self.parent = parent
    	if parent is None :
    		self.executed = False

    def isSafelyExecuted():
    	return False if (self.parent is None) else True if isinstance(self.parent, Reader) and self.parent.executed and self.executed else self.parent.isSafelyExecuted() and self.executed

    def executeParent(self):
    	if not self.parent.executed:
    		self.parent.process()

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'
