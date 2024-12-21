# Version: 1.0
#loading screen in Python
#Helping to create a loading screen in Python by Copilot :)

import time
import random
import os

for i in range(0, 101, 1): #range(start, stop, step)
    os.system('cls') #update the screen
    print("Loading: " + str(i) + "%") #print the percentage
    time.sleep(random.uniform(0.1, 0.5)) #wait for a random time between 0.1 and 0.5 seconds

print("Loading complete!") #print the final message
time.sleep(2) #wait for 2 seconds
os.system('cls') #clear the screen

#end of the code

#Explanation:

#This code is a simple example of a loading screen in Python.
#It uses a for loop to iterate over a range of numbers from 0 to 100, printing the percentage of completion at each step.
#The os.system('cls') command is used to clear the screen and update the displayed percentage.
#The time.sleep() function is used to introduce a delay between each step, creating the effect of a loading screen.
#Finally, a message is printed to indicate that the loading is complete, and the screen is cleared after a short delay.
#Thanks copilot for helping me to create this code.
#copilot is a great tool for generating code snippets and providing suggestions for improving code quality :)