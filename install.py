#!/usr/bin/env python3

#Will raise a error if the following library is not satisfied, Ik they all are built-in modules TwT
try:
    import os
    import shutil
    from time import sleep
    import colorama
    import subprocess
except importError:
    print('Dependecies not satisfied')
    print('Please run "pip install -r requirements.txt" before execucting this script')
    exit(1)

def banner(): #Idk maybe just for some decoration hehe
    green = colorama.Back.GREEN
    red = colorama.Fore.RED
    reset = colorama.Style.RESET_ALL
    os.system('clear')
    print (colorama.Fore.GREEN + f"""
    
/$$$$$$$              /$$      /$$$$$$  /$$ /$$                    
| $$__  $$            | $$     /$$__  $$|__/| $$                    
| $$  \ $$  /$$$$$$  /$$$$$$  | $$  \__/ /$$| $$  /$$$$$$   /$$$$$$$
| $$  | $$ /$$__  $$|_  $$_/  | $$$$    | $$| $$ /$$__  $$ /$$_____/
| $$  | $$| $$  \ $$  | $$    | $$_/    | $$| $$| $$$$$$$$|  $$$$$$ 
| $$  | $$| $$  | $$  | $$ /$$| $$      | $$| $$| $$_____/ \____  $$
| $$$$$$$/|  $$$$$$/  |  $$$$/| $$      | $$| $$|  $$$$$$$ /$$$$$$$/
|_______/  \______/    \___/  |__/      |__/|__/ \_______/|_______/ 
                                                                author: {red}@based_ricky / @Yorubae{reset}                                                                    
          """)

user = os.getlogin()
config_path = f"/home/{user}/Personal-Dotfiles/.config/" 
system_config = f"/home/{user}/.config/"
backup_dir = f"/home/{user}/Personal-Dotfiles/userprev_config"

#Looks whether the repository exists on your Home Directory, I think its pretty unnecessary tho :/
if not os.path.exists(config_path):
    print('Hold up! did you by any chance renamed the directory or you\'re directly using the script without cloning the repo :/\nMan are you fr?')
    exit(1)
else :
    print('Directory Found!')
    sleep(2)

banner() #calling out my banner HAHA
packages = ["fish", "alacritty", "neofetch", "cava", "waybar", "starship", "rofi", "nvim", "swaylock"] #Making a list for the packages :p
def check_dependecy(package): #A function that checks for executeable file in the binary
    try:
        output = subprocess.check_output(['which', package])
        return True
    except subprocess.CalledProcessError:
        return False

#Checking out for the packages if its installed on the system
for package in packages:
    if not check_dependecy(package):
        print(f"{package} is not installed!")
        print()

#Here comes the file manipulation, LOL
for file in os.listdir(config_path): #iterating through the oonfigs files in the repository
    old_path = os.path.join(system_config, file) #Just combining the path with the filename, incase of
    backup_path = os.path.join(backup_dir, file)
    new_path = os.path.join(config_path, file)
    if os.path.isfile(new_path):
        if file in os.listdir(system_config):
            print(f"{file} already Exist in the {system_config}")
            shutil.move(old_path, backup_path)
            print(f'{file} moved to backup folder incase if you wanna restore!')
        shutil.copy(new_path, old_path)
        print(f"{file} moved to {system_config}")
    elif os.path.isdir(new_path):
        if file in os.listdir(system_config):
            print(f"{file} already Exist in the {system_config}")
            shutil.move(old_path, backup_path)
            print(f"{file} moved to {backup_dir} incase you wanna resetore!")
        shutil.copytree(new_path, old_path)
        print(f"{file} moved to {system_config}")
    else:
        print("Error: {new} is not a file neither a dir?!")

