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

import random

class Logic(object):
    """docstring for Logic"""
    def __init__(self):
        print("Init Logic")
        self.dict_objects = {} # dict to store tower list, mob list, etc
        self.dict_objects['towers'] = []
        self.dict_objects['mobs'] = []
        self.dict_objects['bullets'] = []
        #self.dict_objects['towers'].append((200, 200))
        # Map Matrix containing Tiles (own class) with attributes like texture, towerBuildable, etc
        # self.dict_objects['map'] = [[0 for x in range(5)] for x in range(5)]

    def getDictObjects(self):
        return self.dict_objects

    def update(self, dt):
    #def update(self):
        for index, mob in enumerate(self.dict_objects['mobs']):
            x = (mob[0] + int(dt * 60)) % 500
            y = (mob[1] - int(dt * 60)) % 400
            self.dict_objects['mobs'][index] = (x, y)
        #print(self.dict_objects)
        #print(len(self.dict_objects['mobs']))

    def placeTower(self, x, y):
        if((x, y) not in self.dict_objects['towers']):
            self.dict_objects['towers'].append((x, y))
            # later
            # newTower = Tower("Type A", x, y)
            # self.dict_objects['towers'].append(newTower)
            #print("T %s" %self.dict_objects['towers'])

    def placeMob(self, x, y):
        self.dict_objects['mobs'].append((x, y))
        #print("M %s" %self.dict_objects['mobs'])

