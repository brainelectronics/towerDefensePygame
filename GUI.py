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
# 
# 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import pygame

class Window(object):
	"""docstring will be added later"""
	def __init__(self, length, height):
	    self.dict_objects = {}
	    self.myScreen = pygame.display.set_mode((length, height))
	    pygame.display.set_caption("Tower Defense")
	    self.black = (  0,   0,   0)
	    self.white = (255, 255, 255)
	    self.red   = (255,   0,   0)
	    self.green = (  0, 255,   0)
	    self.blue  = (  0,   0, 255)
	    self.myfont = pygame.font.SysFont("monospace", 25)

	def setLogic(self, logic):
		print("Logic set")
		self.logic = logic
		self.dict_objects = self.logic.getDictObjects()

	def render(self, fps):
		"""add a function to draw only the moved elements since last frame"""
		self.myScreen.fill((0, 0, 0)) # clear screen with black
		
		"""still problems working with more than one scaled image"""
		imgBlue=pygame.image.load('blue-dot.png')
		imgBlue = pygame.transform.scale(imgBlue, (20, 20))
		self.myScreen.blit(imgBlue, (50,50))
		
		imgRed=pygame.image.load('red-dot.png')
		imgRed = pygame.transform.scale(imgRed, (20, 20))
		self.myScreen.blit(imgRed, (100,100))

		for  mob in self.dict_objects['mobs']:
			#print("Mob x=%d y=%d" %(mob[0], mob[1]))
			pygame.draw.circle(self.myScreen, self.red, (mob[0], mob[1]), 20, 0)
		
		for tower in self.dict_objects['towers']:
			#print("Tower x=%d y=%d" %(tower[0], tower[1]))
			pygame.draw.circle(self.myScreen, self.blue, (tower[0], tower[1]), 20, 0)

		label = self.myfont.render(("%0.2ffps" %(fps)), 1, (255,255,0))
		self.myScreen.blit(label, (0, 0))

	def drawObjects(self):
		pygame.draw.polygon(self.myScreen, self.green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
		pygame.draw.line(self.myScreen, self.blue, (60,60), (120, 60), 4)
		pygame.draw.line(self.myScreen, self.blue, (120, 60), (60, 120), 4)
		pygame.draw.line(self.myScreen, self.blue, (60, 120), (120, 120), 4)
		pygame.draw.circle(self.myScreen, self.blue, (300, 50), 20, 0)
		pygame.draw.ellipse(self.myScreen, self.red, (300, 200, 40, 80), 1)
		pygame.draw.rect(self.myScreen, self.red, (200, 150, 100, 50))
		
    	#pygame.draw.circle(screen, blue, (300, 50), 20, 0)