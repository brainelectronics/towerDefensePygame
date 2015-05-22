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

	def redraw(self):
		#pass
		#print(self.dict_objects['mobs'])
		#print(self.dict_objects['towers'])
		for mob in self.dict_objects['mobs']:
			#print("Mob x=%d y=%d" %(mob[0], mob[1]))
			pass

		for tower in self.dict_objects['towers']:
			#print("Tower x=%d y=%d" %(tower[0], tower[1]))
			pass
		"""
		for mob in self.dict_objects['mobs']:
			print("Mob x=%d y=%d" %(mob[0], mob[1]))

        for tower in self.dict_objects['towers']:
        	print("Tower x=%d %s y=%d %s" %(tower[0], tower[1]))
        	"""