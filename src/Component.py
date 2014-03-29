#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Component():

    def __init__(self, name) :
    	self.name = name

def createComponent(names):
	comp = Component(names[0])
	return names[1:], comp

if __name__ == "__main__" :

	import string
	names = string.letters + string.digits
	print names

	names, component = createComponent(names)

	print names

	