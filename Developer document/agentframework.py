
# -*- coding: utf-8 -*-
"""
Time: Created on Mon Feb  7 16:50:57 2022
@author: Chongrui Li
@Vesion: Python 3.7
"""
import random

# define a class of points
class Agent:
    
    # Initialize some properties including point, background, x,y coordinates and so on
    def __init__(self,id,environment,agents,y,x,alive):
        self.alive = True
        self.agents = agents
        self.environment = environment
        self.store = 0
        self.id = id
        self.y = y
        self.x = x
        # self.color = color
        # self.x = random.randint(0,99)
        # self.y = random.randint(0,99)
        # Define x,y to be chosen randomly from 0 to 100
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = x 
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x 
        

    # Define a function for descriptive information to be printed on the console
    def __str__(self):
        return "id" + str(self.id) + ", y=" + str(self.y) + ", x=" + str(self.x) + ",  store=" + str(self.store)
    
    # Define a function for point movement, passing the parameter of distance
    # Internal calls function of move_coordinate
    def move(self,d):
        self.x = self.move_coordinate(self.x,d)
        # if (random.random()< 0.5):
        #     self.x = (self.x + 1) % 100
        # else: 
        #     self.x = (self.x - 1) % 100        
        self.y = self.move_coordinate(self.y,d)
        # if (random.random()< 0.5):s
        #     self.y = (self.y + 1) % 100
        # else: 
        #     self.y = (self.y - 1) % 100
    
    # This function is described by a judgment statement,
    # When the random value is less than 0.3, it means that the point does not move ,
    # when it is less than 0.5,  it means moving distance of "d"
    def move_coordinate(self,a,d):
        if random.random() < 0.3:
            return a
        if random.random() < 0.5:
            a = (a + random.randint(1,d)) % 100
        else:
            a = (a - random.randint(1,d)) % 100
        return a
    # The aim of this function is displaying the running track of points. 
    def eat(self): # can you make it eat what is left?
        if  self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    # This function is about points finding nearby points and sharing the relevant information and resources with them.
    def share_with_neighbours(self,neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if (self.id != agent.id):
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
            # print("sharing " + str(dist) + " " + str(ave))
    # Find the distance between the x,y values of the coordinates of the current object and each of the points of loop in the "agents" array
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
