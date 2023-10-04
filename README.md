APT GUI Beta

This Python script provides a graphical user interface (GUI) for managing APT packages on Debian-based Linux distributions. It simplifies common package management tasks and provides a user-friendly interface. Below is an overview of the script's functionality and how to use it.
Features:

Install

    Function: Install a package using apt.
    Usage: Enter the package name (e.g., neofetch) when prompted, and the script will attempt to install it.

Uninstall

    Function: Remove a package using apt.
    Usage: Enter the package name when prompted, and the script will attempt to remove it.

Autoremove

    Function: Automatically remove orphaned packages.
    Usage: Confirm the action when prompted, and the script will remove orphaned packages using apt.
    WARNING! THIS CAN EASILY BRICK YOUR SYSTEM IF YOU DON'T KNOW WHAT YOU ARE DOING! USE WITH CAUTION!

Upgrade

    Function: Upgrade installed packages.
    Usage: Confirm the action when prompted, and the script will upgrade all installed packages using apt.

Distro-Upgrade

    Function: Perform a distribution upgrade.
    Usage: Confirm the action when prompted, and the script will perform a full distribution upgrade using apt.

Cache Update

    Function: Refresh the package cache.
    Usage: Confirm the action when prompted, and the script will update the package cache using apt-get.

Show Details

    Function: Display detailed information about a package.
    Usage: Enter the package name when prompted, and the script will show detailed information using apt show.

Reinstall

    Function: Reinstall a package.
    Usage: Enter the package name when prompted, and the script will attempt to reinstall it using apt.

wget (EXPERIMENTAL! USE AT OWN RISK!)

    Function: Download a file from a URL using wget.
    Usage: Enter the URL to download when prompted, and the script will use wget to download the file.

dpkg (EXPERIMENTAL! USE AT OWN RISK!)

    Function: Install a Debian package (.deb file) using dpkg.
    Usage: Enter the package name (including the path if necessary) when prompted, and the script will attempt to install it using dpkg.

Add PPA (EXPERIMENTAL! USE AT OWN RISK!)

    Function: Add a Personal Package Archive (PPA) repository.
    Usage: Enter the PPA URL when prompted, and the script will add the repository using add-apt-repository.

Search Package

    Function: Search for packages by name or keyword.
    Usage: Enter the package name or keyword when prompted, and the script will search for packages using apt.

Run App (There might be some errors, which you can ignore, it should fully work though, just keep in mind that you have to close the app before exiting the terminal, and while the app is active, you won't be able to use the existing terminal or apt gui app. There seems to be no way around this idk, it's just how it works, at least in ubuntu.)

    Function: Run an application with the user's privileges.
    Usage: This button is used to run a specific application (runapp.py) with the user's privileges. It's useful for running applications that require user-level permissions.

Remove Excess (Safer but less affective than autoremove)

    Function: Remove orphaned packages.
    Usage: Confirm the action when prompted, and the script will remove orphaned packages using deborphan and apt-get purge.

EXIT

    Function: Exit the APT GUI.
    Usage: Click this button to exit the script.

Important Notes

    The script should be run with sudo privileges for package management tasks. If not, it will prompt you to run it with sudo.
    Some actions may require confirmation before proceeding.
    The script provides feedback on the success or failure of each operation using pop-up messages.
    You must NOT copy, remove or change anything in that folder, it could render it useless.

Getting Started

    1: Navigate to the location you saved the folder and then opening it in the terminal. Alternatively, use "cd" command. Then, you should have something like:

    your@username:~/yourfolder/APT-GUI$

    2:Then, just run the install.sh script:

    your@username:~/yourfolder/APT-GUI$ sudo bash install.sh

    3: You are done! The window should spawn!

    4: If you EVER want to use the script again, use the following command:

    sudo python3 apt.py

Compatibility

    The script is designed for Debian-based Linux distributions like Ubuntu and Debian. It checks for compatibility with the distribution during startup.

Disclaimer

    This script should be used with caution, especially when installing or removing packages, or running autoremove, as it requires sudo privileges and can affect or damage your system.
    I AM NOT RESPONSIBLE FOR ANY DAMAGE!

Author

    The APT GUI Beta was created entirely by Ben (@randomappleboi).

Enjoy using this APT package management GUI!

Please do NOT redistribute, redistribute a changed version or do anything else than using it normally. You are allowed to modify it, to improve it or to change it, but you must NOT redistribute said version without MY PERMISSION.
Should you encounter any issues, please let me know:
    @randomappleguy (Twitter/X) [I prabably won't respond]
    @randomapple (github) [I prabably won't respond]
    randomappleboi@protonmail.com (e-Mail)
    @mathunitedx (YouTube) [most likely response]
