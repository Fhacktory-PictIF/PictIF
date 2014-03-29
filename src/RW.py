#!/usr/bin/env python
# -*- coding: utf-8 -*-
from component import Component
from IO import O, ImageData
import os, time

class Reader(Component):

    def __init__(self, name):
        Component.__init__(self, name)
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
    def __init__(self, name):
        Component.__init__(self, name)
        self.path = ""
        self.osef = "File path:string,etc."
        
    def process():
        O.write(self.images, self.path, "")
        self.executed = True