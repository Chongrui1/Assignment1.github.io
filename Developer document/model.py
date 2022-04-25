# -*- coding: utf-8 -*-
"""
Time:Created on Mon Feb  7 16:49:14 2022
@author: Chongrui Li
@Vesion: Python 3.7
"""
# Importing some packages
import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation  
import matplotlib
import tkinter
import catsframework
import requests
import bs4
import math
# def distance_between(agents_row_a, agents_row_b):
    # return (((agents_row_a.x - agents_row_b.x)**2) +
            # ((agents_row_a.y - agents_row_b.y)**2)) ** 0.5


# Reading  raster background files for coordinate systems
environment=[]
f = open('in.txt', newline ='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
# The outer loop iterates over an array and the inner loop iterates over the values read from the csc file
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
#         print(value)
    
# size = len(environment)    
# matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
    
# Set various relevant variable parameters, for example: the number of points are ten
random.seed(0)
num_of_agents = 10
num_of_iterations = 10
num_of_cats = 1
neighbourhood = 100
agents = []
cats = []
carry_on = True	
alive = True
# Thess codes are about IO output file (write of IO) 
# f1 = open("C:\Programming GIS//anotherfile.txt", 'w')
# writer = csv.writer(f1, delimiter=' ')
# for row in environment:
#     writer.writerow(row) # List of values.
# f1.close()


# a = agentframework.Agent(1)
# b = agentframework.Agent(2)
# print(a)
# print(b)
# matplotlib.pyplot.show() 


# Import the specified data file, and print out relevant information on the console
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# After running, Setting a trigger button to run the model when the button is clicked, and the style of the graph.
matplotlib.use('TkAgg') 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
root.wm_title("Model of cat catching rats")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)  




# Select the points in the coordinate system from the specified data file above.
for i in range(num_of_agents):
      y = int(td_ys[i].text)
      x = int(td_xs[i].text)
      agents.append(agentframework.Agent(i,environment,agents,y,x,alive))
      
for j in range(num_of_cats):
      y = int(td_ys[j].text)
      x = int(td_xs[j].text)
      cats.append(catsframework.Cats(j,cats,y,x,'Blue')) 




      
def update(frame_number):
    global carry_on
    fig.clear()
    d = 2
    distance = 2
    neighbourhood = 1
    
    
    # Calling the various functions setting in the Agents class and catsframework through Array "agent" and "cats"       
    # Display each point data in the imported background file 
       
    
    for j in range(num_of_cats):
        for i in range(num_of_agents): 
            x = agents[i].x - cats[j].x 
            y = agents[i].y - cats[j].y 
            dis = math.sqrt((x**2) + (y**2))  
            if dis > 30:
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c= "Black")
            else:
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker = 'x', alpha = 0.5,  c= "White")
                matplotlib.pyplot.title('Scatter plot of cat catching rates') 
                matplotlib.pyplot.xlabel('Variables x') 
                matplotlib.pyplot.ylabel('Variables y')     
        
    for i in range(num_of_agents): 
        print(agents[i])
        agents[i].move(d)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
    for j in range(num_of_cats):
        cats[j].move(distance)
        print(cats[j])   
            
      
    
    # animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    for j in range(num_of_cats):
        matplotlib.pyplot.scatter(cats[j].x,cats[j].y, color = cats[j].color)
    
    
# This code, which shows agents points in the coordinate system during the learning process, has been removed and has been subsequently improved
# for i in range(num_of_agents):
#     # agents.append([random.randint(0,99),random.randint(0,99)])
#     print(agents[i])
# d = size
# Move the agents.
    # for j in range(num_of_iterations):       
            # agents[i].eat()
            # if random.random() < 0.5:
            #     agents[i][0] = (agents[i][0] + 1) % 100
            # else:
            #     agents[i][0] = (agents[i][0] - 1) % 100
            # if random.random() < 0.5:
            #     agents[i][1] = (agents[i][1] + 1) % 100
            # else:
            #     agents[i][1] = (agents[i][1] - 1) % 100
            # print(agents[0])
    # answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    # print(answer)
        
        
        
    # show of the background information of read in the model after the run
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)      
    # matplotlib.pyplot.show()

# a function about number of times the point moves in the animation
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a		
        a = a + 1
        
# Define a function about content displayed in the menu line of the model
# and calls to other functions regarding the presentation of animations
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)   
    canvas.draw() 

    
    
model_menu.add_command(label="Run Programme", command=run) 
tkinter.mainloop()       




# these codes are used to find the distance between two agents    
# for agents_row_a in agents:
    # for agents_row_b in agents:
        # distance = distance_between(agents_row_a,agents_row_b)
    
