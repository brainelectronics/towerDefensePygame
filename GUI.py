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
	    #img=pygame.image.load('blue-dot.png')
		#self.myScreen.blit(img, (0,0))

		for  mob in self.dict_objects['mobs']:
			#print("Mob x=%d y=%d" %(mob[0], mob[1]))
			pygame.draw.circle(self.myScreen, self.red, (mob[0], mob[1]), 20, 0)
		
		for tower in self.dict_objects['towers']:
			#print("Tower x=%d y=%d" %(tower[0], tower[1]))
			pygame.draw.circle(self.myScreen, self.blue, (tower[0], tower[1]), 20, 0)

		label = self.myfont.render(("%0.2ffps" %(fps)), 1, (255,255,0))
		self.myScreen.blit(label, (0, 0))
    	#pygame.draw.circle(screen, blue, (300, 50), 20, 0)

