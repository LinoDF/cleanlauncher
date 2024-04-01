# import libraries
import minecraft_launcher_lib
import os
from os import system
import subprocess
# set window title
system("title " + "CleanLauncher")
# set launcher path
winusr = os.environ["USERNAME"]
minedir = "C://Users//" + winusr + "//AppData//Roaming//.cleanlauncher"
verdir = "C://Users//" + winusr + "//AppData//Roaming//.cleanlauncher//versions"
if os.path.exists(verdir) == False:
    os.makedirs(verdir)
# list game versions
print("Latest release: " + minecraft_launcher_lib.utils.get_latest_version()["release"])
print()
print("Latest snapshot: " + minecraft_launcher_lib.utils.get_latest_version()["snapshot"])
print()
print("Installed versions:")
for element in minecraft_launcher_lib.utils.get_installed_versions(minedir):
    print(element["id"])
print()
# set game version and username
minever = input("Version: ")
print()
mineusr = input("Userame: ")
print()
settings = {
    "username": mineusr,
    "uuid": "",
    "token": ""
    }
# generate version json
minevers = minecraft_launcher_lib.utils.get_available_versions(minedir)
jver = open(verdir + "//versions.json", "w")
print(minevers, file = jver)
jver.close()
# install and run game
print("Please wait...")
minecraft_launcher_lib.install.install_minecraft_version(minever, minedir)
runmine = minecraft_launcher_lib.command.get_minecraft_command(minever, minedir, settings)
subprocess.run(runmine)
