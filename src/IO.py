#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ntpath, time
from SimpleCV import Image

class O():
    """Output mechanism"""
    def __init__(self):
        pass

    def write(self, images, path, ComponentId):
        for image in images:
            image.image.save(path + image.name + ComponentId + image.extension)

class ImageData():
    """Image object"""
    def __init__(self, path):
        self.path = path
        self.date = time.ctime(os.path.getctime(path))
        self.name = os.path.splitext(os.path.basename(path))[0]
        self.extension = os.path.splitext(path)[1]
        self.image = None
        self.suffixes = ""

    def load(self):
        self.image = Image(self.path)

    def unload(self):
        del self.image
