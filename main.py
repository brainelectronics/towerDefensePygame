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

# import ConfigHannes
# import GUI
# import KI
# import Queue
import pygame
import GUI
import Logic

# ueberpruefen, ob die optionalen Text- und Sound-Module geladen werden konnten.
if not pygame.font: print('Error: pygame.font module could not be loaded!')
if not pygame.mixer: print('Fehler pygame.mixer module could not be loaded!')


class TowerDefense(object):
	"""docstring for TowerDefense"""
	pygame.init()

	def __init__(self):
		print("Init")
		pygame.init()
		self.screen = pygame.display.set_mode((800, 600))
		self.logic = Logic.Logic()
		self.gui = GUI.Window()
		self.gui.setLogic((self.logic))
		
	def main(self):

	    # Initialisieren aller Pygame-Module und 
	    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).
	    #pygame.init()
	    #screen = pygame.display.set_mode((800, 600))
	    
	    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.
	    pygame.display.set_caption("Pygame-Tutorial: Tilemap")
	    pygame.mouse.set_visible(1)
	    pygame.key.set_repeat(1, 30)

	    # Clock Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.
	    clock = pygame.time.Clock()
	    
	    # Wir erstellen eine Tilemap.
	    #map = Tilemap.Tilemap()
	    
	    # Die Schleife, und damit unser Spiel, läuft solange running == True.
	    running = True
	    while running:
	        # Framerate auf 30 Frames pro Sekunde beschränken.
	        # Pygame wartet, falls das Programm schneller läuft.
	        clock.tick(30)

	        # screen Surface mit Schwarz (RGB = 0, 0, 0) füllen.
	        self.screen.fill((0, 0, 255))

	        
	        event = pygame.event.poll()
	        if event.type == pygame.QUIT:
	        	running = False

	        if event.type == pygame.KEYDOWN:
	        	if event.key == pygame.K_ESCAPE:
	        		pygame.event.post(pygame.event.Event(pygame.QUIT))

	        if event.type == pygame.MOUSEBUTTONDOWN:
	        	#print("orginal Left mouse click at (%d, %d)" %event.pos)
	        	x = int(event.pos[0] / 50) * 50
	        	y = int(event.pos[1] / 50) * 50

	        	if event.button == 1: # left
	        		print("left click at (" +str(x) + "," + str(y) + ")")
	        		self.logic.placeTower(x,y)
	        	elif event.button == 3: # right
	        		print("rigth click at (" +str(x) + "," + str(y) + ")")
	        		self.logic.placeMob(x,y)
	        
	        """
	        # Alle aufgelaufenen Events holen und abarbeiten.
	        for event in pygame.event.get():
	            # Spiel beenden, wenn wir ein QUIT-Event finden.
	            if event.type == pygame.QUIT:
	                running = False
	            
	            # Wir interessieren uns auch für "Taste gedrückt"-Events.
	            if event.type == pygame.KEYDOWN:
	                # Wenn Escape gedrückt wird posten wir ein QUIT-Event in Pygames Event-Warteschlange.
	                if event.key == pygame.K_ESCAPE:
	                    pygame.event.post(pygame.event.Event(pygame.QUIT))
	                
	                # Alle Tastendrücke auch der Tilemap mitteilen.
	               # map.handle_input(event.key)
	        	
	        	if event.type == pygame.MOUSEBUTTONDOWN:
	        		print("clicked")
	        		if event.button == 1:
	        			print("left click")
	        		elif event.button == 3:
	        			print("rigth click")
	       	"""
	        # Die Tilemap auf die screen-Surface rendern.
	        #map.render(screen)
	        #print(clock) # print the current fps
	        #print(pygame.mouse.get_pos())
	        #print(pygame.mouse.get_pressed())
	        self.logic.update(1/30)
	        self.gui.redraw()

	        # Inhalt von screen anzeigen
	        pygame.display.flip()

if __name__ == '__main__':
    towerDefense = TowerDefense()
    towerDefense.main()
