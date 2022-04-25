"""
Time: Created on Mon Feb  7 16:50:57 2022
@author: Chongrui Li
@Vesion: Python 3.7
"""

import random

# define a class of "Cats"
class Cats:
     def __init__(self,ia,cats,y,x,color):
        self.ia = ia
        self.cats = cats
        self.x = x
        self.y = y
        self.color = color
        
     def move(self,distance):
        self.x = self.move_coordinate(self.x,distance)
        self.y = self.move_coordinate(self.y,distance)
    
     def move_coordinate(self,a,distance):
         if random.random() < 0.2:
             return a
         if random.random() < 0.5:
            a = (a + random.randint(1,distance)) % 100
         else:
            a = (a - random.randint(1,distance)) % 100
         return a
