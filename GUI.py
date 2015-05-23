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
#
# All rights reserved.
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
from pygame import gfxdraw
import math

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
	    self.towerPoints = []
	    self.rotation = 0

	def setLogic(self, logic):
		print("Logic set")
		self.logic = logic
		self.dict_objects = self.logic.getDictObjects()

	def render(self, fps):
		"""add a function to draw only the moved elements since last frame"""
		self.myScreen.fill((0, 0, 0)) # clear screen with black
		
		imgBlue=pygame.image.load('blue-dot.png')
		imgBlue = pygame.transform.scale(imgBlue, (20, 20))
		self.myScreen.blit(imgBlue, (50,50))

		imgRed=pygame.image.load('red-dot.png')
		imgRed = pygame.transform.scale(imgRed, (20, 20))
		self.myScreen.blit(imgRed, (100,100))
		
		if self.rotation <= 360:
			self.rotation += 1
		else:
			self.rotation = 0
		
		for  mob in self.dict_objects['mobs']:
			#print("Mob x=%d y=%d" %(mob[0], mob[1]))
			pygame.draw.circle(self.myScreen, self.red, (mob[0], mob[1]), 20, 0)
		
		for tower in self.dict_objects['towers']:
			#print("Tower x=%d y=%d" %(tower[0], tower[1]))
			#pygame.draw.circle(self.myScreen, self.blue, (tower[0], tower[1]), 20, 0)
			self.drawTower(tower[0], tower[1], 20, self.rotation, 0)

		label = self.myfont.render(("%0.2ffps" %(fps)), 1, (255,255,0))
		self.myScreen.blit(label, (0, 0))

	def drawTower(self, posX, posY, rad, deg, shoot):
		#tower base
		pygame.gfxdraw.filled_polygon(self.myScreen, 
			((posX, posY+rad), (posX+rad, posY+rad/2), (posX+rad, posY-rad/2), 
				(posX, posY-rad), (posX-rad, posY-rad/2), (posX-rad, posY+rad/2)),
				self.blue)
		"""
		#border
		pygame.gfxdraw.aapolygon(self.myScreen, 
			((posX, posY+rad), (posX+rad, posY+rad/2), (posX+rad, posY-rad/2), 
				(posX, posY-rad), (posX-rad, posY-rad/2), (posX-rad, posY+rad/2)),
				self.red)
		"""
		"""
		pygame.gfxdraw.filled_polygon(self.myScreen, 
			((posX, posY-rad/2), (posX+rad/2, posY+rad/2), (posX+rad/2, posY-rad/2)), 
			self.red)
		"""
		pygame.gfxdraw.circle(self.myScreen, posX, posY, 10, self.red)
		#pygame.draw.line(surface, color, (startX, startY), (endX, endY), width)
		pygame.draw.line(self.myScreen, self.red,
			(posX, posY), (posX+int(rad*math.sin(deg*math.pi/180)), posY+int(rad*math.cos(deg*math.pi/180))), 5)
		#pygame.gfxdraw.circle(self.myScreen, posX, posY-rad/2, 20, self.red)
		#pygame.gfxdraw.circle(self.myScreen, posX+rad/2, posY+rad/2, 20, self.red)
		#filled_trigon(surface, x1, y1, x2, y2, x3, y3, color)

	def drawObjects(self):
		#pygame.draw.polygon(self.myScreen, self.green, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
		#pygame.gfxdraw.filled_circle(self.myScreen, 146,0, 10, self.red)
		#y		*1
		#	*6		*2
		#	*5		*3 90deg
		#		*4 0deg
		#		x
		#pygame.gfxdraw.filled_polygon(self.myScreen, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)), self.white)
		pygame.gfxdraw.filled_circle(self.myScreen, 146,0, 10, self.red)
		#pygame.draw.line(self.myScreen, self.blue, (60,60), (120, 60), 4)
		#pygame.draw.line(self.myScreen, self.blue, (120, 60), (60, 120), 4)
		#pygame.draw.line(self.myScreen, self.blue, (60, 120), (120, 120), 4)
		#pygame.gfxdraw.aacircle(self.myScreen, 300, 50, 200, self.blue)
		#pygame.gfxdraw.filled_circle(self.myScreen, 300, 100, 200, self.blue)
		#pygame.gfxdraw.pie(self.myScreen, 300, 150, 200, 0, 270, self.blue)
		#pygame.gfxdraw.pie(surface, x, y, r, start, end, color)
		#pgyame.gfxdraw.aacircle(surface, x, y, r, color)
		pygame.draw.circle(self.myScreen, self.red, (300, 200), 20, 0)
		pygame.draw.ellipse(self.myScreen, self.red, (300, 200, 40, 80), 3)
		pygame.draw.rect(self.myScreen, self.green, (200, 150, 100, 50))
		#imgRect = pygame.image.load('blue-rect.png')
		#imgRect = pygame.transform.scale(imgRect, (20,30))
		#imgRect = pygame.transform.rotate(imgRect, 45)
		#self.myScreen.blit(imgRect, (50, 50))
		
    	#pygame.draw.circle(screen, blue, (300, 50), 20, 0)