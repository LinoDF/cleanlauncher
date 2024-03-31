
# import libraries
import minecraft_launcher_lib
import os
import subprocess
# set launcher path
winusr = os.environ["USERNAME"]
minedir = "C://Users//" + winusr + "//AppData//Roaming//.cleanlauncher"
verdir = "C://Users//" + winusr + "//AppData//Roaming//.cleanlauncher//versions"
if os.path.exists(verdir) == False:
    os.makedirs(verdir)
#set game version and username
minever = input("Version: ")
mineusr = input("Name: ")
settings = {
    "username": mineusr,
    "uuid": "The UUID",
    "token": "The acces token"
}
# generate version json
minevers = minecraft_launcher_lib.utils.get_available_versions(minedir)
jver = open(verdir + "//versions.json", "w")
print(minevers, file = jver)
jver.close()
# install and run game
minecraft_launcher_lib.install.install_minecraft_version(minever, minedir)
runmine = minecraft_launcher_lib.command.get_minecraft_command(minever, minedir, settings)
subprocess.run(runmine)