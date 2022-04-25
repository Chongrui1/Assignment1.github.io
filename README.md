# Assigement1_Scatter plot of a cat catching rats
## Description of programming content:
This is a model of the cat catching rates,ten rates moving through an area and have their own track route of movement,
cats catching the nearby mouses, which the distance from it is less then 30 meters.Within this certain distance, the cat will catch this rate.
If the cat capturing successfully a rate, a white x can be seen in the image, if it cannot, a black point can be seen in the image.
The user can run the menu by clicking on "Programme" to get an effect of presentation. 

## Description of each document:
mode.py : This file is the main runtime file for this program,the content of the code includes the implementation of various functions, for instance,loading of coordinate systems and reading of background image.There is also code about running front-end pages directly.There are also calls to various functions in other documents, such as movement, eating, interaction between agent points, etc.

agentframework.py: This file contains the initialisation of the various 'rat' parameters.Various other functions,such as eat, move_coordinate, and most importantly, the interact with each agent points, etc.
 
catsframework.py: This file contains the initialisation of the various 'cats' parameters.the functions are similar to the 'agentframework'.

## How to run it?
Open the model.py document, run it,  in the dialogue of the "Model of cat catching rates", click on the "Model",then click on the the "Run Programme", this programme will run successfully.

