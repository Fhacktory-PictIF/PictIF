#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import Component
from IO import O
import time

class Splitter(Component):
    """Splits one stream into two based on one criteria"""
    def __init__(self):
        Component.__init__(self)
        self.description = "Splits one data stream into two data streams depending whether they match some specific criteria"
        criteria = None
        self.images2 = None

    def process(self):
        self.images = []
        self.images2 = []

        for image in self.parent.images:
            # TODO define split criteria
            pass

        self.executed = True


class RowFilter(Component):
    """Filters some rows based on certains criteria 
    such as date, time, extension"""
    def __init__(self):
        Component.__init__(self)
        self.description = "Excludes from data stream files matching any of user's criteria"
        self.criteria = None
        self.time_relative = -1 # (-1) before is default value, 0 is equal and 1 is after
        self.time_reference = None
        self.extensions = None
        self.extension_keep = True

    def set_time_reference(self, time_reference):
        self.time_reference = time_reference
        self.extensions = None

    def set_extensions(self, extensions):
        self.time_reference = None
        self.extensions = extensions

    def process(self):
        if self.images is None:
            self.images = []
        tempI = set(self.images + self.parent.images)
        tempO = set()
        if self.time_reference is not None:
            for image in tempI:
                if self.time_relative == 1:
                    if self.time_reference < image.date:
                        tempO.add(image)
                elif self.time_relative == -1:
                    if self.time_reference > image.date:
                        tempO.add(image)
                elif self.time_relative == 0:
                    if self.time_reference == image.date:
                        tempO.add(image)
        elif self.extensions is not None:
            if not self.extension_keep:
                tempO = tempO.union(set([im for im in self.parent.images if im.extension in self.extensions]))
            else:
                tempO = tempO.union(set([im for im in self.parent.images if im.extension not in self.extensions]))
        self.images = list(tempO)
        
class Joiner(Component):
    """Joins two streams into one"""
    def __init__(self):
        Component.__init__(self)
        self.description = "Joins two data streams into one avoiding duplicates."
        self.parent2 = None
    
    def setParent2(self, parent):
        self.parent2 = parent
        if parent is None :
            self.executed = False

    def process(self):
        self.images = list(set(self.parent.images + self.parent2.images))
        self.executed = True