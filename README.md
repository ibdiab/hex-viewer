# hex-viewer
A CLI-based python program allowing the user to pick a file and view it in hexadecimal. This supports files of any size and writes the output to a text file for debugging and analysis.

## INSTALLATION INSTRUCTIONS
1. If you don't have python installed, install it here: https://www.python.org/
  - For MacOS users, check if you have python installed with
    
    ```
    python3 --version
    ```
    If this command fails or prompts you to install dev tools, install it via homebrew

    ```
    brew install python3
    ```
  - For Linux users, check if you have python installed with
    
    ```
    python3 --version
    ```
    If this command fails, update your system to get the latest packages and then install it via your package manager:

    **Debian/Ubuntu**
    
    ```
    sudo apt update && sudo apt upgrade && sudo apt install python3
    ```
    **Fedora**
    
    ```
    sudo dnf upgrade && sudo dnf install python3
    ```
    **Arch**
    
    ```
    sudo pacman -Syu python
    ```
    **Other Distributions**
    If your distro isn't listed here, please install it via your distros package manager.
    
2. Install `Hex_Viewer.py` from the repository.
   
3. You may then open the file in your preferred IDE or follow the instructions below to run it via terminal depending on your OS:
   
4. On **Windows**, open command prompt or PowerShell and navigate to the directory you installed this. For example:
   
    ```
    cd C:\Users\user\Downloads
    ```
    
Run the script with the following command:

    py Hex_Viewer.py
    
On **MacOS/Linux**, open terminal and navigate to the directory you installed it:
  - MacOS: ex.
    
    ```
    cd /Users/user/Downloads
    ```
  - Linux: ex.
    
    ```
    cd /home/user/Downloads
    ```
From there, give the script executable permissions and then run it with

    chmod +x Hex_Viewer.py && ./Hex_Viewer.py

## USAGE
1. Enter the file's name. If it's not in the same directory, enter the absolute path to the file (INCLUDE THE FILE EXTENSION)
   - Windows Example: `C:\Users\user\Desktop\example.dll` Make sure you're entering your actual file's path. These are examples for guidance.
   - Mac OS Example: /Users/user1/Documents/game.iso` Make sure you're entering your actual file's path. These are examples for guidance.
   - Linux Example (Debian, Arch, Fedora, etc.): /home/user/Desktop/example3.txt` Make sure you're entering your actual file's path. These are examples for guidance.

2. From there, feel free to view the hexadecimal code or open the file ending in `.hex.txt` for further analysis and debugging if you wish. It's created in the same directory as where the script was ran.

## PLANNED FEATURES
- Color coding specific patterns
- GUI for easier use
- Importing existing HEX patterns and exporting them
- Editing the HEX code and syncing the results
