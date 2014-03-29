#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import Component
from IO import O
import time

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
        self.criteria = None
        self.time_relative = before # before is default value
        self.time_reference = None


    def setTimeReference(time):
    	self.time_reference = time
        
    def process():
    	if self.time_reference is not None:
	        for image in self.parent.images:
	            # if image.date 
	            pass
	            # TODO WIP
        
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