#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from IO import O, ImageData

nbComponents = 0

def generateId():
    global nbComponents
    nbComponents += 1
    return nbComponents

class Component():
    ioComponents = dict(Reader='Picture Reader', Writer='Picture Writer')
    processors = dict(Cropper='Cropper', GrayScale='Gray Scale', ChromaKey='Chromakey')
    selectors = dict(RowFilter='File Filter', Joiner='Joiner', Splitter='Splitter')
    statistics = []
    #classmere.__subclasses__() return list

    components = dict(ioComponents='I/O', processors='Processors', selectors='Selectors', statistics='Statistics')

    def __init__(self) :
    	self.parent = None
    	self.id = generateId()
    	self.images = None
    	self.executed = False
        self.description = ""

    def setParent(self,parent):
    	self.parent = parent
    	if parent is None :
    		self.executed = False

    def isSafelyExecuted(self):
    	return False if (self.parent is None) else True if isinstance(self.parent, Reader) and self.parent.executed and self.executed else self.parent.isSafelyExecuted() and self.executed

    def executeParent(self):
    	if not self.parent.executed:
    		self.parent.process()

    def process():
    	print 'Abstract class'

    def showOutput():
    	print 'print treated images'

class Reader(Component):

    def __init__(self):
        Component.__init__(self)
        self.description = "Creates a data stream from a file or a folder and its subfolders."
        self.pathes = None
        self.length = None
        self.key_points = []
        self.mean_colors = []

    def setPathes(self, pathes):
        self.pathes = pathes

    def process(self):
        self.read(self.pathes)
        self.length = len(self.images)
        for image in self.images:
            image.load()
        self.key_points = [i.image.findKeypoints() for i in self.images]
        self.mean_colors = [k.meanColor() for k in self.key_points]
        self.executed = True

    def read(self, pathes):
        for path in pathes:
            images = []
            if os.path.isfile(path):
                # print "Considering file1 ", path
                images.append(ImageData(path))
            elif os.path.isdir(path):
                # print "Considering directory ", path
                for dirname, dirnames, filenames in os.walk(path):
                    # print "Directory ", dirname," has subfolders ", dirnames
                    # print "Directory ", dirname," has subfiles ", filenames
                    for filename in filenames:
                        # print "Considering file2 ", filename, " of ", dirname
                        img = ImageData(os.path.join(dirname, filename))
                        images.append(img)
            self.images = images

class Writer(Component):
    """Writes pics on disc"""
    def __init__(self):
        Component.__init__(self)
        self.description = "Writes the content of the data stream's content in a specified path."
        self.path = ""
        self.osef = "File path:string,etc."

    def process():
        O.write(self.images, self.path, "")
        self.executed = True
