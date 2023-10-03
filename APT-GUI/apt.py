import tkinter as tk
import subprocess
from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from tkinter.ttk import Style
from tkinter.simpledialog import askstring
from tkinter.messagebox import askokcancel, showinfo, showerror
from PIL import ImageTk, Image
import os
import distro
import sys

# Check if the script is run with sudo privileges
if os.geteuid() != 0:
    showerror("Error!", "This script must be run with sudo privileges.\n If the 'Run App' popup already appeared, and if this\nthis appears after pressing the 'Run App' buttons, please ignore this.")
    sys.exit(1)

dist_name = distro.linux_distribution(full_distribution_name=False)[0].lower()

if 'ubuntu' in dist_name or 'debian' in dist_name:
    print(f"The Linux distribution '{dist_name}' is compatible!")
else:
    root = tk.Tk()
    root.withdraw()
    showerror("Error", f"The Linux distribution '{dist_name}' is not compatible with this program.")
    exit(1)



def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

script_dir = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(script_dir, 'logo.png')

path = os.getcwd()

print(path)

root = tk.Tk()
frame = tk.Frame(root, width="600", height="300")
frame.pack(fill=BOTH, expand=True)
root.title('APT GUI Beta - made by Ben @randomappleboi')

background_frame = Frame(frame, bg="black")
background_frame.place(relwidth=1, relheight=1)


root.iconphoto(False, tk.PhotoImage(file='ico.png'))


try:
    image2 = Image.open(logo_path)
    logo = ImageTk.PhotoImage(image2)
except FileNotFoundError:
    print("Logo image not found")



def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

messagebox_style = Style()
messagebox_style.configure('Custom.TButton', background='black', foreground='white')

def install():
    Package = askstring('Package', 'What package are you trying to install? (e.g. neofetch)')
    if Package:
        showinfo('Installing Package', 'Hi, We will now attempt to install ' + str(Package) + '.')
        try:
            result = subprocess.run([f"sudo apt -y install {Package}"], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                showinfo('Success!', 'Package installation completed successfully!')
            else:
                showinfo('Error', 'Package installation failed :-(\n' + result.stderr)
        except subprocess.CalledProcessError as e:
            showinfo('Error', 'Package installation failed :-(\n' + e.stderr)

def remove():
    PackageRMV = askstring('Package', 'What package are you trying to remove?')
    if PackageRMV:
        showinfo('Remove Package', 'Hi, We will now attempt to remove ' + str(PackageRMV) + '.')
    try:
        result = subprocess.run([f"sudo apt -y remove {PackageRMV}"], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            showinfo('Success!', 'Package removal completed successfully!')
        else:
            showinfo('Error', 'Package removal failed.\n' + result.stderr)
    except subprocess.CalledProcessError as e:
        showinfo('Error', 'Package removal failed.\n' + e.stderr)

def autoremove():
    if True:
        askokcancel('Autoremove Package', 'Hi, We will now attempt to autoremove')
    try:
        result = subprocess.run([f"sudo apt -y autoremove"], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            showinfo('Success!', 'Autoremoval completed successfully!')
        else:
            showinfo('Error', 'Autoremoval failed.\n' + result.stderr)
    except subprocess.CalledProcessError as e:
        showinfo('Error', 'Autoremoval failed.\n' + e.stderr)

def upgrade():
    if True:
        askokcancel('Upgrade', 'We will now try to upgrade all packages.')
    try:
        result = subprocess.run(([f"sudo", "apt", "-y", "upgrade"]))
        if result.returncode == 0:
            showinfo('Success!', 'Upgrade Successful!')
        else:
            showinfo('Upgrade','Upgrade failed!\n' + result.stderr)
    except subprocess.CalledProcessError as e:
        showinfo('Upgrade', 'Upgrade failed!\n' + e.stderr)

def dist_upgrade():
    if True:
        askokcancel('Upgrade', 'Trying to perform Distro-Upgrade!')
    try:
        result = subprocess.run(([f"sudo", "apt", "-y", "full-upgrade"]))
        if result.returncode == 0:
            showinfo('Upgrade','Distro-Upgrade successful!')
        else:
            showinfo('Upgrade', 'Distro-Update failed!\n' + result.stderr)
    except subprocess.CalledProcessError as e:
        showinfo('Upgrade', 'Distro-Upgrade failed!\n' + e.sterr)

def cacherefresh():
    if True:
        askokcancel('Cache', 'Attempting cache refresh!')
    try:
        result = subprocess.run(([f"sudo", "apt-get", "-y", "update"]))
        if result.returncode == 0:
            showinfo('Cache', 'Cache refresh successful!')
        else:
            showinfo('Cache', 'Cache refresh failed!\n' + result.stderr)
    except subprocess.CalledProcessError as e:
        showinfo('Cache', 'Cache refresh failed!\n' + e.stderr)

def showdetail():
    package_name = askstring('Package Info', 'What package do you want to now more about?')
    if package_name:
        try:
            result = subprocess.run(['sudo', 'apt', 'show', package_name], capture_output=True, text=True, check=True)
            if result.returncode == 0:
                package_info = result.stdout
                messagebox.showinfo('Package Info', package_info)
            else:
                error_message = result.stderr
                messagebox.showerror('Error', f'Error retrieving package info:\n{error_message}')
        except subprocess.CalledProcessError as e:
            messagebox.showerror('Error', f'Error retrieving package info:\n{e.stderr}')

def reinstall():
    Package = askstring('Package', 'What package are you trying to reinstall?')
    if Package:
        showinfo('Installing Package', 'Hi, We will now attempt to reinstall ' + str(Package) + '.')
        try:
            result = subprocess.run([f"sudo apt -y reinstall {Package}"], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                showinfo('Success!', 'Package reinstallation completed successfully!')
            else:
                showinfo('Error', 'Package reinstallation failed. :-(\n' + result.stderr)
        except subprocess.CalledProcessError as e:
            showinfo('Error', 'Package reinstallation failed. :-(\n' + e.stderr)

def exit():
    response = askokcancel('Exit', 'Do you really want to quit?')
    if response:
        sys.exit()

def advwget():
    url = askstring("Download URL", "Enter the URL to download:")
    if url:
        try:
            result = subprocess.run([f"wget", "-t", "0", {url}], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                showinfo("Download Complete", "File downloaded successfully! :-(")
            else:
                showinfo("Download Failed", "Failed to download the file :-(\n" + result.stderr)
        except subprocess.CalledProcessError as e:
            showinfo("Download Failed", "Failed to download the file :-(\n" + e.stderr)

def dpkg_install():
    dpkg_package = askstring("Install Debian Package", "Enter the package name")
    if dpkg_package:
        try:
            result = subprocess.run(["sudo", "dpkg", "-i", dpkg_package], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                showinfo("Installation Complete", "Package installed successfully!")
            else:
                showinfo("Installation Failed", "Failed to install the package :-(\n" + result.stderr)
        except subprocess.CalledProcessError as e:
            showinfo("Installation Failed", "Failed to install the package :-(\n" + e.stderr)

def add_ppa():
    ppa_url = askstring("Add PPA", "Enter the URL of the PPA you want to add")
    if ppa_url:
        try:
            result = subprocess.run(["sudo", "add-apt-repository", f"ppa:{ppa_url}"], capture_output=True, text=True, shell=True)
            if result.returncode == 0:
                subprocess.run(["sudo", "apt-get", "update"])
                showinfo("PPA Added", f"The PPA '{ppa_url}' has been added successfully!")
            else:
                showinfo("PPA Addition Failed", "Failed to add the PPA :-(\n" + result.stderr)
        except subprocess.CalledProcessError as e:
            showinfo("PPA Addition Failed", "Failed to add the PPA :-(\n" + e.stderr)

def search_package():
    query = simpledialog.askstring("Search Packages", "Enter the package name or keyword:")
    if query:
        try:
            result = subprocess.check_output(["apt", "search", query], text=True)
            messagebox.showinfo("Package Search Result", result)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error searching for packages:\n{e}")

def runapp():
    username_cmd = ['logname']
    username = subprocess.check_output(username_cmd, text=True).strip()
    cmd = ['sudo', '-u', username, 'python3', 'runapp.py']
    subprocess.run(cmd, check=True)

def rmorphans():
    try:
        orphaned_packages = subprocess.check_output(["deborphan"], text=True).splitlines()
        if orphaned_packages:
            confirmation = messagebox.askquestion("Confirmation", f"Found {len(orphaned_packages)} orphaned packages.\nDo you want to remove them?")
            if confirmation == "yes":
                for package in orphaned_packages:
                    subprocess.run(["sudo", "apt-get", "purge", "-y", package])
                messagebox.showinfo("Success", "Orphaned packages have been removed successfully.")
            else:
                messagebox.showinfo("Canceled", "Orphaned package removal has been canceled.")
        else:
            messagebox.showinfo("No Orphaned Packages", "No orphaned packages found on your system.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

logon = Label(background_frame, image=logo, bg="black")  
logon.place(x=150, y=30)

description = Label(background_frame, text="A simple apt GUI script", fg="white", bg="black")
description.place(x=350, y=150)

descriptiontwo = Label(background_frame, text='Advanced', fg='grey', bg='black')
descriptiontwo.place(x=60, y=200)

inst = tk.Button(background_frame,
                 text="Install",
                 fg='white',
                 bg='black',
                 command=install,
                 relief=tk.FLAT,
                 activebackground='#5685A1',
                 state='normal')
inst.place(x=60, y=300)

remv = tk.Button(background_frame,
                 text="Uninstall",
                 fg='white',
                 bg='black',
                 relief=tk.FLAT,
                 activebackground='#5685A1',
                 command=remove)
remv.place(x=230, y=300)

armv = tk.Button(background_frame,
                 text="Autoremove",
                 activebackground='#5685A1',
                 fg='white',
                 relief=tk.FLAT,
                 bg='black',
                 command=autoremove)
armv.place(x=400, y=300)

upgr = tk.Button(background_frame,
                 text="Upgrade",
                 fg='white',
                 relief=tk.FLAT,
                 bg='black',
                 command=upgrade,
                 activebackground='#5685A1',
                 state='normal')
upgr.place(x=60, y=440)

dupgr = tk.Button(background_frame,
                  text="Distro-Upgrade",
                  activebackground='#5685A1',
                  fg='white',
                  relief=tk.FLAT,
                  bg='black',
                  state='normal',
                  command=dist_upgrade)
dupgr.place(x=230, y=440)

care = tk.Button(background_frame,
                 text="Cache Update",
                 relief=tk.FLAT,
                 activebackground='#5685A1',
                 fg='white',
                 bg='black',
                 command=cacherefresh,)
care.place(x=400, y=440)

show = tk.Button(background_frame,
                  text="Show details",
                  activebackground="#5685A1",
                  fg='white',
                  bg='black',
                  relief=tk.FLAT,
                  state='normal',
                  command=showdetail
                  )
show.place(x=60, y=370)

reinst = tk.Button(background_frame,
                   text='Reinstall',
                   activebackground='#5685A1',
                   fg='white',
                   bg='black',
                   relief=tk.FLAT,
                   command=reinstall)
reinst.place(x=230, y=370)

ext = tk.Button(background_frame,
                text='EXIT',
                activebackground='#FF1B58',
                activeforeground='white',
                bg='black',
                relief=tk.FLAT,
                command=exit,
                fg='#FF0055')
ext.place(x=400, y=510)

wget = tk.Button(background_frame,
                 text='wget',
                 activebackground='#455E6C',
                 fg='grey',
                 relief=tk.FLAT,
                 bg='black',
                 command=advwget)
wget.place(x=400, y=230)

dpm = tk.Button(background_frame,
                text='dpkg',
                activebackground='#455E6C',
                bg='black',
                fg='grey',
                relief=tk.FLAT,
                command=dpkg_install)
dpm.place(x=60, y=230)

addppa = tk.Button(background_frame,
                   text='Add PPA',
                   activebackground='#455E6C',
                   fg='grey',
                   bg='black',
                   relief=tk.FLAT,
                   command=add_ppa)
addppa.place(x=230, y=230)

search = tk.Button(background_frame,
                   text='Search Package',
                   activebackground='#5685A1',
                   bg='black',
                   relief=tk.FLAT,
                   fg='white',
                   command=search_package)
search.place(x=400, y=370)

runbutton = tk.Button(background_frame,
                      text='Run App',
                      activebackground='#5685A1',
                      bg='black',
                      relief=tk.FLAT,
                      fg='white',
                      command=runapp)
runbutton.place(x=60, y=510)

orphanremove = tk.Button(background_frame,
                      text='Remove Excess',
                      activebackground='#5685A1',
                      bg='black',
                      relief=tk.FLAT,
                      fg='white',
                      command=rmorphans)
orphanremove.place(x=230, y=510)


root.resizable(False, False)

center_window(root, 600, 580)

root.mainloop()
