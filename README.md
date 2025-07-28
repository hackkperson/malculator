#Memz Trojan Calculator
#Overview
#The Memz Trojan Calculator is a malicious script disguised as a simple calculator application. It performs various harmful actions on the target machine, including taking screenshots, stealing passwords, spamming pop-up messages, and deleting critical registry keys. The collected data is sent to a specified SMB share on your network.

#Features
#Calculator Interface: Presents a simple calculator interface to the user, making the malicious activities less suspicious.
#Screenshot Capture: Takes screenshots of the target machine's screen and saves them to a specified SMB share.
#Password Stealing: Searches for and steals stored passwords from Internet Explorer and saves them to a text file in the SMB share.
#Pop-Up Spamming: Spams the target machine with pop-up messages, disrupting the user's experience.
#Registry Key Deletion: Deletes critical registry keys, which can potentially brick the target machine.
#Persistent Execution: Adds itself to the Windows startup folder to ensure it runs on system boot.
#Requirements
#Python 3.x
#Pillow library for image handling
#PyAutoGUI library for automating GUI interactions
#Installation
#Install the required libraries:
#bash
#pip install pillow pyautogui
#Save the script as calculator.py.
#Usage
#Run the script on the target machine:
#bash
#python calculator.py
#The script will present a simple calculator interface to the user.
#Enter commands directly in the console to perform actions:
#screenshot: Takes a screenshot and saves it to the SMB share.
#passwords: Steals stored passwords and saves them to a text file in the SMB share.
#popups: Spams pop-up messages on the target machine.
#delete: Deletes critical registry keys, potentially bricking the PC.
#exit: Exits the script.
#Configuration
#The script dynamically discovers the local IP address of the machine running it and uses it to specify the SMB share path. Ensure that the SMB share is set up correctly on your network.
#Disclaimer
#This script is for educational purposes only. Use it at your own risk and ensure you have permission to test on the target machines.
