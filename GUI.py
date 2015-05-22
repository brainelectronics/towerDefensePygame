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
	def __init__(self):
	    self.dict_objects = {}
	    self.myScreen = pygame.display.set_mode((800, 600))

	def setLogic(self, logic):
		print("Logic set")
		self.logic = logic
		self.dict_objects = self.logic.getDictObjects()

	def render(self):
		self.myScreen.fill((255, 0, 0))
		img=pygame.image.load('blue-dot.png')
		self.myScreen.blit(img, (0,0))
    	#self.screen.blit(img,(0,0))
    	#pygame.draw.circle(screen, (255,0,0), (300, 50), 20, 0)

    	#for mob in self.dict_objects['mobs']:
    	#	print("Mob x=%d y=%d" %(mob[0], mob[1]))

