import tkinter as tk
from tkinter import filedialog
import sys
import ctypes
import os
import random

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

# reopen
file.close()
file = open(file_path, "r", encoding = 'utf-8')

# name the new file
for num in range(1,1000):
    if not os.path.isfile(file_path[:-5] + "_random_" + str(num) + "].osu"):
        new_file_path = file_path[:-5] + "_random_" + str(num) + "].osu"
        ver = num
        break

new_file = open(new_file_path, "a", encoding = 'utf-8')

for line in file:
    if "Version:" in line.strip():
        new_file.write(line.strip() + "_random_" + str(ver) + "\n")
        break
    else:
        new_file.write(line)

for line in file:
    new_file.write(line)
    if line.strip() == "[HitObjects]":
        break

for line in file:
    splited = line.split(",")
    if splited[3] == "5" or splited[3] == "1":
        if splited[4] == "0" or splited[4] == "8":
            if random.randint(0,1) == 0:
                new_file.write(splited[0] + "," + splited[1] + "," + splited[2] + "," + splited[3] + ",0," + splited[5] + "\n")
            else:
                new_file.write(splited[0] + "," + splited[1] + "," + splited[2] + "," + splited[3] + ",8," + splited[5] + "\n")
        elif splited[4] == "4" or splited[4] == "12":
            if random.randint(0,1) == 0:
                new_file.write(splited[0] + "," + splited[1] + "," + splited[2] + "," + splited[3] + ",4," + splited[5] + "\n")
            else:
                new_file.write(splited[0] + "," + splited[1] + "," + splited[2] + "," + splited[3] + ",12," + splited[5] + "\n")
        else:
            new_file.write(line)
    else:
        new_file.write(line)

file.close()
new_file.close()