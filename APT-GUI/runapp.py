import os
from tkinter import *
from tkinter import messagebox
import sys
import subprocess
from tkinter.simpledialog import askstring
from tkinter.messagebox import showerror

if os.geteuid() == 0:
    showerror("Error!", "This script shouldn't be ran with sudo privileges.")
    sys.exit(1)

application = askstring('Run App', 'What application do you want to run? (e.g. firefox)')

subprocess.run([application])

sys.exit