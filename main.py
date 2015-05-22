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

# import ConfigHannes

import pygame
import GUI
import Logic

'''check correct optinal module loading '''
if not pygame.font: print('Error: pygame.font module could not be loaded!')
if not pygame.mixer: print('Fehler pygame.mixer module could not be loaded!')


class TowerDefense(object):
	"""init all modules and start main loop"""
	#pygame.init() #obsolete

	def __init__(self):
		print("Init")
		pygame.init()
		#self.screen = pygame.display.set_mode((800, 600)) #outsourced to GUI
		self.logic = Logic.Logic()
		self.gui = GUI.Window(500, 400) # maybe editable via setup file
		self.gui.setLogic((self.logic))
		#self.playtime = 0.0
		self.targetFPS = 60
		
	def main(self):	    
	    pygame.mouse.set_visible(1)
	    pygame.key.set_repeat(1, 30)

	    # Clock Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
	    clock = pygame.time.Clock()
	    	    
	    # Die Schleife, und damit unser Spiel, läuft solange running == True.
	    running = True
	    while running:
	    	'''limit frames to targetFPS, pygame waits here if it would be faster'''
	        clock.tick(self.targetFPS)
	        self.targetFPS = clock.get_fps() #get_fps
	        #self.playtime += self.targetFPS/1000.0

	        '''mouse interaction only works with poll for me'''
	        event = pygame.event.poll()	
	        if event.type == pygame.QUIT:
	        	running = False

	        if event.type == pygame.KEYDOWN:
	        	if event.key == pygame.K_ESCAPE:
	        		pygame.event.post(pygame.event.Event(pygame.QUIT))

	        if event.type == pygame.MOUSEBUTTONDOWN:
	        	x = int(event.pos[0] / 50) * 50
	        	y = int(event.pos[1] / 50) * 50

	        	if event.button == 1: # left
	        		print("left click at (" +str(x) + "," + str(y) + ")")
	        		self.logic.placeTower(x,y)
	        	elif event.button == 3: # right
	        		print("rigth click at (" +str(x) + "," + str(y) + ")")
	        		self.logic.placeMob(x,y)
	        
	        """
	        # fetch all occured events and solve them
	        for event in pygame.event.get():
	            # exit loop on quit event
	            if event.type == pygame.QUIT:
	                running = False
	            
	            # eveluate also the keyboard events
	            if event.type == pygame.KEYDOWN:
	                # add quit event on K_ESCAPE to quue
	                if event.key == pygame.K_ESCAPE:
	                    pygame.event.post(pygame.event.Event(pygame.QUIT))
	                
	               # map.handle_input(event.key)
	        	
	        	if event.type == pygame.MOUSEBUTTONDOWN:
	        		print("clicked")
	        		if event.button == 1:
	        			print("left click")
	        		elif event.button == 3:
	        			print("rigth click")
	       	"""
	       	# prevent from zero division
	       	if self.targetFPS > 0:
	       		dt = 1.0/self.targetFPS
	       	else:
	       		dt = 1.0/30

	       	#print(dt)
	        self.logic.update(dt) #
	        #self.gui.render((self.screen)) #geht
	        '''render now next frame, parameter for FPS info label'''
	        self.gui.render((self.targetFPS))
	        # show on screen window
	        pygame.display.flip()

if __name__ == '__main__':
    towerDefense = TowerDefense()
    towerDefense.main()
