from tkinter import * 
from tkinter.ttk import *
import psutil
import time

# for sleep 
minutes = 5
seconds = minutes * 60

# creating Tk window 
def display(percent, plugged):
    master = Tk() 

    # adding title to the tkinter window
    master.title("Surya's Battery Assistant")

    # setting geometry of tk window 
    master.geometry("300x150") 

    # label for the text below    
    l1 = Label(master, text = "Please Disconnect Charger") 
    l1.config( anchor = CENTER) 
    l1.pack()
    
    # label to display battery percentage and plugged status
    l2_message = f'{percent}% | {plugged}'
    l2 = Label(master, text = l2_message) 
    l2.pack()

    # Button which when clicked on destroys the loop
    b2 = Button(master, text = "OK", command = master.destroy) 
    b2.place(relx = 0.5, rely = 0.5, anchor = CENTER) 

    # infinite loop which is required to 
    # run tkinter program infinitely 
    # until an interrupt occurs 
    mainloop() 

while(True):

    # gets the battery status
    battery = psutil.sensors_battery()
    
    # unpacks battery percent 
    percent = battery.percent

    if percent >= 95:

        # gets the plugged status from battery
        plugged = battery.power_plugged 

        plugged = "Plugged In" if plugged else "Not Plugged In"

        # if plugged in and battery is >= 95 display the message 
        if plugged == "Plugged In":
            display(percent, plugged)

            # sleep for 5 minutes and loop back again
            time.sleep(seconds)
    # if battery percent is not >= 95 loops back and checks again