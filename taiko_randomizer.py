import tkinter as tk
from tkinter import filedialog
import sys
import ctypes
import os

# file selection
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# if the user pressed cancel
if not file_path:
    sys.exit(0)

# open file
file = open(file_path, "r", encoding = 'utf-8')

# file check
ext = os.path.splitext(file_path)[-1].lower()

# wrong extension
if ext != ".osu":
    ctypes.windll.user32.MessageBoxW(0, "Incorrect file extension", "Error", 1)
    file.close()
    sys.exit(0)

# unknown file format
if not file.readline().startswith("osu file format"):
    ctypes.windll.user32.MessageBoxW(0, "Incorrect file content", "Error", 1)
    file.close()
    sys.exit(0)

hasMode = False
# not taiko mode
for line in file:
    if line.startswith("Mode:"):
        if not line.strip() == "Mode: 1":
            ctypes.windll.user32.MessageBoxW(0, "Not taiko mode", "Error", 1)
            file.close()
            sys.exit(0)
        hasMode = True
        break

# if there is no Mode: 
if not hasMode:
    ctypes.windll.user32.MessageBoxW(0, "Incorrect file content", "Error", 1)
    file.close()
    sys.exit(0)

file.close()
file = open(file_path, "r", encoding = 'utf-8')

for num in range(1,1000):
    if not os.path.isfile(file_path + "_random_" + str(num)):
        new_file_path = file_path + "_random_" + str(num)
        break

new_file = open(new_file_path, "a", encoding = 'utf-8')

for line in file:
    new_file.write(line)
    if line.strip() == "[HitObjects]":
        break

for line in file:
    