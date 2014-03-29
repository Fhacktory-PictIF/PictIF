#!/usr/bin/env python
# -*- coding: utf-8 -*-
from component import Component
from IO import I, O

class Reader(Component):

	def __init__(self, name):
		Component.__init__(self, name)
		self.input = I()
		self.output = O()
		self.length = None
		self.key_points = []
		self.mean_colors = []

	def process(self):
		#TODO : replace with I.read()
		img_input = self.input.read("../test/")

		self.length = len(img_input)
		self.key_points = [i.image.findKeypoints() for i in img_input]
		self.mean_colors = [k.meanColor() for k in self.key_points]
		self.executed = True