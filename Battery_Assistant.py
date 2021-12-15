# Note if any of the below packages is not installed in your system then install it
# Syntax "pip install <packagename>" where <packagename> can be playsound, psutil, time
# open command prompt type command "pip install pyttsx3"
# open command prompt type command "pip install psutil"
# from playsound import playsound
import pyttsx3
from tkinter import *
from tkinter.ttk import *
import psutil
import time

# for sleep 
minutes = 5
seconds = minutes * 60
engine = pyttsx3.init()

# creating Tk window 
def display(percent, plugged):
    master = Tk() 

    # adding title to the tkinter window
    master.title(" Battery Assistant ")
    x_coordinate = 460
    y_coordinate = 300  
    # setting geometry of tk window 
    master.geometry("%dx%d+%d+%d" %(300,100,x_coordinate,y_coordinate)) 

    # label for the text below    
    l1 = Label(master, text = "Please disconnect the charger") 
    l1.config( anchor = CENTER) 
    l1.pack()
    
    # label to display battery percentage and plugged status
    l2_message = f'{percent}% | {plugged}'
    l2 = Label(master, text = l2_message) 
    l2.pack()

    # Button which when clicked on destroys the loop
    b2 = Button(master, text = "OK", command = master.destroy) 
    b2.place(relx = 0.5, rely = 0.7, anchor = CENTER) 

    # infinite loop which is required to 
    # run tkinter program infinitely 
    # until an interrupt occurs 
    mainloop() 

while(True):

    # gets the battery status
    battery = psutil.sensors_battery()

    if battery:
        # unpacks battery percentage
        percent = battery.percent
        # engine.say(f'System is at {percent} percent battery level')
        # engine.runAndWait()

        if percent >= 95:
        # gets the plugged status from battery
            plugged = battery.power_plugged 

            plugged = "Plugged In" if plugged else "Not Plugged In"

            # if plugged in and battery is >= 95 display the message 
            if plugged == "Plugged In":      
                display(percent, plugged)
                engine.say(f'System is at {percent} percent battery level')
                engine.say(f'Please disconnect the charger')
                engine.runAndWait()
                # sleep for 5 minutes and loop back again
                time.sleep(seconds)
                
            # if battery percent is not >= 95, checks for the below condition.
        if percent <= 20:
            # gets the plugged status from battery
            plugged = battery.power_plugged 

            plugged = "Plugged In" if plugged else "Not Plugged In"
            
            # if not plugged and battery is <=20 display the message 
            if plugged == "Not Plugged In":
                engine.say(f'System is at {percent} percent battery level')
                engine.say(f'Please connect the charger')
                engine.runAndWait()
                display(percent, plugged)
                # sleep for 5 minutes and loop back again
                time.sleep(seconds)
                
        # if battery percent is not <= 20 loops back and checks again

    else:
        engine.say("Cannot determine the battery level")
        engine.runAndWait()
        break