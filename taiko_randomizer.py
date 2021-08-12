import tkinter as tk
from tkinter import filedialog
import sys
import ctypes
import os

# file selection
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# open file
file = open("file_path", "r")

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
        if not line == "Mode: 1":
            ctypes.windll.user32.MessageBoxW(0, "Not taiko mode", "Error", 1)
            file.close()
            sys.exit(0)
        hasMode = True
        break

if not hasMode:
    ctypes.windll.user32.MessageBoxW(0, "Incorrect file content", "Error", 1)
    file.close()
    sys.exit(0)