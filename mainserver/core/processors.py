#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from component import Component
from IO import O, ImageData
from SimpleCV import Color
import cv2

class Cropper(Component):

	attr_description = Component.attr_description + "output:O:output writer,x:int:top left point's abscisse of cropping rectangle,\
		y:int:top left point's ordonate of cropping rectangle,width:int:width of cropping rectangle,\
		height:int:height of cropping rectangle"

	description = "Component for cropping images. It takes as input a list of images and returns the list of cropped images"

	def __init__(self):
		Component.__init__(self)
		self.output = O()
		self.x = 0
		self.y = 0
		self.width = 100
		self.height = 100

	def process(self):

		if not self.executed and (self.parent is not None):
			self.executeParent()

			self.images = self.parent.images
			for im in self.images:
				im.image = im.image.crop(self.x,self.y,self.width,self.height)
			
			self.output.write(self.images,'../../test/cropped/',self.id)

			self.executed = True

class GrayScale(Component):

	attr_description = Component.attr_description + "output:O:output writer,degree:int:output images darkness"

	description = "Component for turning the images into gray scale. It takes as input a list of images and returns the list of gray images"

	def __init__(self):
		Component.__init__(self)
		self.output = O()
		self.degree = 1

	def process(self):

		if not self.executed and (self.parent is not None):
			self.executeParent()

			self.images = self.parent.images

			for im in self.images:
				(red, green, blue) = im.image.splitChannels(False)
				im.image = (red.toGray() + green.toGray() + blue.toGray()) / self.degree

			self.executed = True
			
			self.output.write(self.images,'../../test/binarized/',self.id)

class ChromaKey(Component):

	def __init__(self):
		Component.__init__(self)
		self.green_screen = ImageData("../test/greenScreen.jpg")
		self.green_screen.load()
		self.background = ImageData("../test/landscape.jpg")
		self.background.load()
		self.green_screen.image = self.green_screen.image.scale(self.background.image.width, self.background.image.height)

	def process(self):

		if not self.executed and (self.parent is not None):
			self.executeParent()

			mask = self.green_screen.image.hueDistance(color=Color.GREEN).binarize()
			
			result = (self.green_screen.image - mask) + (self.background.image - mask.invert())
			result.show()
			time.sleep(10)

class FacesDetector(Component):

	def __init__(self):
		Component.__init__(self)
		self.image = ImageData("../../test/people.jpg")
		self.cascade = cv2.CascadeClassifier('../../XML/haarcascade_frontalface_default.xml')
		self.image.load()
		self.output = O()

	def process(self):

		if not self.executed and self.parent is not None:
			self.executeParent()

			img = cv2.imread("../../test/people.jpg")
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ret,thresh = cv2.threshold(gray,127,255,0)
			faces = self.cascade.detectMultiScale(gray, 1.3, 5)
			contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
			for (x,y,w,h) in faces:
				cv2.ellipse(img, (x + w / 2,y + h / 2),(w / 2,h / 2), 0, 0, 360,(255,0,0),2)
				#for c,k in zip(contours,range(len(contours))):
				#	if cv2.pointPolygonTest(c,(x,y),False) > -1:
				#		cv2.drawContours(img, contours, k, (0,255,0), 3)
			

			cv2.imshow('img',img)
			cv2.waitKey(0)
			cv2.destroyAllWindows()


if __name__ == "__main__" :

	import string
	suffixes = string.letters + string.digits
	"""binarizer = GrayScale(suffixes[0])
	suffixes = suffixes[1:]
	binarizer.process()
	chroma = ChromaKey(suffixes[0])
	suffixes = suffixes[1:]
	chroma.process()"""
	detector = FacesDetector()
	suffixes = suffixes[1:]
	detector.process()
