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

myScreen = pygame.display.set_mode((500, 400))

bulletList = pygame.sprite.Group()
targetList = pygame.sprite.Group()
allSpriteList = pygame.sprite.Group()

towerBase = pygame.image.load('towerBase.png')
towerBase = pygame.transform.scale(towerBase, (50, 50))
towerBase = towerBase.convert_alpha()
towerBaseRect = towerBase.get_rect()

towerTower = pygame.image.load('towerTower.png')
towerTower = pygame.transform.scale(towerTower, (30, 30))
towerTower = towerTower.convert_alpha()
towerTowerRect = towerTower.get_rect()

towerBullet = pygame.image.load('red-dot.png')

black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)

class Window(object):
	"""docstring will be added later"""
	def __init__(self, length, height):
	    self.dict_objects = {}
	    pygame.display.set_caption("Tower Defense")
	    self.black = (  0,   0,   0)
	    self.white = (255, 255, 255)
	    self.red   = (255,   0,   0)
	    self.green = (  0, 255,   0)
	    self.blue  = (  0,   0, 255)
	    self.myfont = pygame.font.SysFont("monospace", 25)
	    self.rotation = 0
	    """
	    self.thisMob = TheMob(red)
	    self.thisMob.rect.x = 300
	    self.thisMob.rect.y = 50
	    targetList.add(self.thisMob)
	    allSpriteList.add(self.thisMob)
	    """

	def setLogic(self, logic):
		print("Logic set")
		self.logic = logic
		self.dict_objects = self.logic.getDictObjects()

	def render(self, fps):
		"""render all mobs, towers and other elements on the screen"""
		"""add a function to draw only the moved elements since last frame"""
		myScreen.fill(black)

		if self.rotation <= 360:
			self.rotation += 1
		else:
			self.rotation = 0
		
		for  mob in self.dict_objects['mobs']:
			#print("Mob x=%d y=%d" %(mob[0], mob[1]))
			pygame.draw.circle(myScreen, self.red, (mob[0], mob[1]), 20, 0)
			
		
		for tower in self.dict_objects['towers']:
			#print("Tower x=%d y=%d" %(tower[0], tower[1]))
			#pygame.draw.circle(self.myScreen, self.blue, (tower[0], tower[1]), 20, 0)
			#myScreen.blit(self.towerBase, (tower[0]-25, tower[1]-25))
			"""
			self.myScreen.blit(
				(pygame.transform.rotate(self.towerTower, self.rotation).get_rect(center=self.towerTower.center)), 
				(210, 210))
			"""
			self.thisTower = TheTower(tower[0], tower[1], -220)
			# don't shoot twice at 0, because 0 == 360
			if (self.rotation%30 == 0) and (self.rotation != 0):
				#print("10 frames")
				self.thisTower.shoot()
			self.thisTower.removeBullet()

		allSpriteList.update()

		label = self.myfont.render(("%0.2ffps" %(fps)), 1, green)
		myScreen.blit(label, (0, 0))
		self.printSprites(allSpriteList)

	def printSprites(self, theSprites):
		theSprites.draw(myScreen)

class TheMob(pygame.sprite.Sprite):
	"""docstring for TheMob"""
	number = 0 # use this to count down
	def __init__(self, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([50, 50], pygame.SRCALPHA)
		self.mobImage = pygame.transform.scale(towerBase, (50, 50))
		self.image.blit(self.mobImage, (0, 0))
		self.rect = self.mobImage.get_rect()
		self.number = TheMob.number
		TheMob.number += 1
		print("Placed mob %d" %TheMob.number)

class Block(pygame.sprite.Sprite):
	""" This class represents the block. """
	def __init__(self, color):
	# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)#(self, self.groups)
		self.image = pygame.Surface([20, 15])
		self.image.fill(color)
		self.rect = self.image.get_rect()

class TheTower(object):
	"""docstring for TheTower"""
	def __init__(self, posX, posY, rotation):
		self.posX = posX
		self.posY = posY
		self.rotation = rotation
		# print("The Tower %d %d %d %d" 
		#	%(self.posX, self.posY, self.rotation, self.fire))
		self.placeBase()
		self.drawHead()

	def placeBase(self):
		myScreen.blit(towerBase, (self.posX-25, self.posY-25))

	def drawHead(self):
		rotatedSurf =  pygame.transform.rotate(towerTower, 180+self.rotation)
		rotatedRect = rotatedSurf.get_rect(center=(self.posX, self.posY))
		# draw rotatedSurf with the corrected rect so it gets put in the proper spot
		myScreen.blit(rotatedSurf, rotatedRect)

	def shoot(self):
		self.aBullet = Bullet(self.rotation)
		self.aBullet.rect.x = self.posX-5
		self.aBullet.rect.y = self.posY-5
		allSpriteList.add(self.aBullet)
		bulletList.add(self.aBullet)

	def removeBullet(self):
		for self.aBullet in bulletList:
			if self.aBullet.rect.y < -10:
				bulletList.remove(self.aBullet)
				allSpriteList.remove(self.aBullet)
				print("Removed bullet %d" %self.aBullet.number)


class Bullet(pygame.sprite.Sprite):
	"""docstring for Bullet"""
	"""add a unique number for each bullet, not needed"""
	number = 0
	def __init__(self, angle):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10, 10], pygame.SRCALPHA)
		# self.image.fill(blue)
		# add image rather than only colored surface
		self.bulletImage = pygame.transform.scale(towerBullet, (10, 10))
		# self.bulletImage = pygame.transform.rotate(self.bulletImage, angle)
		# pygame.gfxdraw.aacircle(self.image, 5, 5, 5, red)
		self.image.blit(self.bulletImage, (0, 0))
		self.rect = self.bulletImage.get_rect()
		self.number = Bullet.number
		Bullet.number += 1
		self.angle = angle
		print("Placed bullet %d" %Bullet.number)

	def update(self):
		"""Move the bullet"""
		self.rect.x -= int(3*math.sin(self.angle*math.pi/180))
		self.rect.y -= int(3*math.cos(self.angle*math.pi/180))

class SomeClass(object):
	"""test class and functions"""
	def __init__(self, arg):
		self.arg = arg
		
	def draw(self, posX, posY, rad, deg, shoot):
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