#!/usr/bin/env python
# -*- coding: utf-8 -*-
from component import Component
from IO import O, ImageData
import os

class Reader(Component):

    def __init__(self, name):
        Component.__init__(self, name)
        self.path = None
        self.length = None
        self.key_points = []
        self.mean_colors = []

    def setPath(self, path):
        self.path = path

    def process(self):
        self.read(self.path)
        self.length = len(self.images)
        for image in self.images:
            image.load()            
        self.key_points = [i.image.findKeypoints() for i in self.images]
        self.mean_colors = [k.meanColor() for k in self.key_points]
        self.executed = True

    def read(self, path):
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
        print len(self.images)

class Writer(Component):
    """Writes pics on disc"""
    def __init__(self, name):
        Component.__init__(self, name)
        self.path = ""
        
    def process():
        O.write(self.images, self.path, "")
        self.executed = True

class Splitter(Component):
    """Splits one stream into two based on one criteria"""
    def __init__(self, name):
        Component.__init__(self, name)
        criteria = None
        self.images2 = None

    def process():
        self.images = []
        self.images2 = []

        for image in self.parent.images:
            # TODO define split criteria
            pass

        self.executed = True


class RowFilter(Component):
    """Filters some rows based on certains criteria 
    such as date, time, extension"""
    def __init__(self, name):
        Component.__init__(self, name)
        criteria = None
        self.images2 = None

    def process():
        
        pass
        
class Joiner(Component):
    """Joins two streams into one"""
    def __init__(self, name):
        Component.__init__(self, name)
        self.parent2 = None
    
    def setParent2(parent):
        self.parent2 = parent
        if parent is None :
            self.executed = False

    def process():
        self.images = self.parent.images + self.parent2.images
        self.executed = True