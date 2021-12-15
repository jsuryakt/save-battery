# `Save Battery`

Leaving the battery plugged in when FULLY-CHARGED will reduce its useful life. 

That is, the maximum capacity of the battery will decline, thereby making a "full charge" refer to a state with less energy than a "full charge" previously denoted.  Note, however, that in general a lithium ion's battery life is measured in "charge cycles." This term refers to the charging and discharging of the battery; that is, do each of these once, and that is one "charge cycle." 

Thus, in order to maximize the length of time over which your battery remains able to hold enough of a charge to be useful, I would suggest minimizing the time that the battery remains plugged in while fully charged. While constantly discharging and recharging fully would be better than leaving the battery plugged in, the better treatment is to not have the battery plugged in.

## About the Script

To notify User about the battery when it exceeds a certain limit or deceeds certain limit to `Save Battery Life`

### Battery_Assistant.py
https://github.com/jsuryakt/save-battery/blob/master/Battery_Assistant.py

This Python file contains the actual code to check if the battery is exceeding a certain limit or not and also the tkinter code for the window.

#### I Converted the Python script to a batch file using the following,
#### 1. Create a notepad file
#### 2. Enter the following in the file
```
"Location where your Python executable exists" "Location where your Python script is saved"
pause
```
Example:-
```
"C:\Users\Jayasurya\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe" "C:\Users\Jayasurya\Desktop\Battery Assistant\Battery_Assistant.py"
pause
```
#### 3. Save the file with extension .bat

 Example:- Battery_Assistant.bat
 
 https://github.com/jsuryakt/save-battery/blob/master/Battery_Assistant.bat
 
Now run and check if the .bat file executes.

Okay, now if everything is fine, we can continue to create a VBScript file, so that we don't have to run the batch file everytime and make the Batch window invisible. VBScript will be silently running in the background.

#### To convert it into a VBScript, follow the below steps,
#### 1. Create a new file in Notepad,
#### 2. Copy paste the below code and change the location,
```
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "Location of batch file" & Chr(34), 0
Set WshShell = Nothing
```
#### Change the location to where your batch file exists.

Example:-
```
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "C:\Users\Jayasurya\Desktop\Battery Assistant\Battery_Assistant.bat" & Chr(34), 0
Set WshShell = Nothing
```
#### 3. Save the file with extension .vbs

Example:- Battery_Assistant.vbs

https://github.com/jsuryakt/save-battery/blob/master/battery_assistant.vbs

Now, we have our VBScript, but everytime we restart the computer we have to run the script again.
To overcome this problem, we have a simple solution.

#### Make script run on Windows StartUp,
#### 1. Create a shortcut of the .vbs file by right clicking on the .vbs file.
#### 2. Click Windows + R, Run window will popup and enter *shell:startup* and hit on Enter. A new window should popup.
#### 3. Now copy/cut the .vbs shortcut created and paste it in the window.

## Voila, Battery Assistant will be up and running everytime you start the system without having to run the script.
## Want to Contribute, if you find any bug or want to upgrade a feature,
Follow these steps:
- Fork the project.
- Create a new branch.
- Make your changes and write tests when practical.
- Commit your changes to the new branch.
- Send a pull request.
