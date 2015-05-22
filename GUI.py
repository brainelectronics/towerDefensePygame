# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# ----------------------------------------------------------------------------
# Tower Defense
# Copyright XD (c) 2015 Python Course TUM
# Abid, Mohamed
# Eckl, Tobias
# Fauser, Jonas
# Scharpf, Jonas
# Schmid, Johannes
# All rights reserved.
import pygame


class Window(object):
	def __init__(self):
	    self.dict_objects = {}


	def setLogic(self, logic):
		print("Logic set")
		self.logic = logic
		self.dict_objects = self.logic.getDictObjects()

	

