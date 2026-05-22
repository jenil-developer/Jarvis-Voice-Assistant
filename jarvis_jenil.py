import sys
import os

base_python = r"C:\Users\Victus\AppData\Local\Python\pythoncore-3.14-64"

win32_folder = os.path.join(base_python, "Lib", "site-packages", "win32")
win32_lib_folder = os.path.join(base_python, "Lib", "site-packages", "win32", "lib")
sys32_folder = os.path.join(base_python, "Lib", "site-packages", "pywin32_system32")

if win32_folder not in sys.path: sys.path.insert(0, win32_folder)
if win32_lib_folder not in sys.path: sys.path.insert(0, win32_lib_folder)

try:
    os.add_dll_directory(base_python)
    os.add_dll_directory(win32_folder)
    os.add_dll_directory(sys32_folder)
except:
    pass

import tkinter as tk
import pyttsx3
import datetime
import webbrowser

try:
    engine = pyttsx3.init()
except Exception as e:
    print(f"Jarvis Active hone me dikkat: {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    greeting = "Hello Master Jenil"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Master Jenil!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master Jenil!")
    else:
        speak("Good Evening Master Jenil!")
    
    today_day = datetime.datetime.now().strftime("%A")
    today_date = datetime.datetime.now().strftime("%B %d")
    
    engine.say(greeting)
    engine.say(f"Today is{today_day}")
    engine.say(f"and the date is{today_date}")
    engine.say("I am Jarvis.How Can I Help You Today?")

    engine.runAndWait()

def open_yt():
    speak("Opening Youtube, Jenil")
    webbrowser.open("https://youtube.com")

def open_google():
    speak("Opening Google")
    webbrowser.open("https://google.com")

root = tk.Tk()
root.title("Master Jenil's Jarvis")
root.geometry("350x400")
root.configure(bg='#0f172a') 

tk.Label(root, text="🤖 JARVIS AI", font=("Courier", 24, "bold"), bg='#0f172a', fg='#38bdf8').pack(pady=30)

btn_style = {"font": ("Arial", 11, "bold"), "width": 18, "pady": 8, "bd": 0}

tk.Button(root, text="Wake Up Jarvis 🗣️", bg='#38bdf8', fg='black', command=wish_me, **btn_style).pack(pady=10)
tk.Button(root, text="Open YouTube 📺", bg='#ef4444', fg='white', command=open_yt, **btn_style).pack(pady=10)
tk.Button(root, text="Open Google 🔍", bg='#10b981', fg='white', command=open_google, **btn_style).pack(pady=10)

root.mainloop()
