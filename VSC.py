"""Automated process to start up my computer"""

# Import modules
import subprocess

# Define the commands to be executed by subprocess
command1 = r"C:\Users\rayde\AppData\Local\Programs\Microsoft VS Code\Code.exe"
command2 = r"C:\Program Files\Logitech Gaming Software\LCore.exe"
command3 = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

# Define the URL's to be opened by webbrowser
url1 = "https://mail.google.com/mail/u/0/?hl=nl&shva=1#inbox"
url2 = "https://www.linkedin.com/feed/"
url3 = "https://github.com/"
url4 = "https://www.google.com/"

# start subprocesses command1, Visual Studio Code
vsc = subprocess.Popen([command1])

# Open chrome window, select ray profile and open pages
# Url1
chrome1 = subprocess.Popen([command3, "--profile-directory=Default", "--window-size=800,600", "--new-window", url1])
# Url2
##chrome1 = subprocess.Popen([command3, "--profile-directory=Default", "--window-size=800,600", url2])
# Url3
##chrome1 = subprocess.Popen([command3, "--profile-directory=Default", "--window-size=800,600", url3])
# Url4
# #chrome1 = subprocess.Popen([command3, "--profile-directory=Default", "--window-size=800,600", url4])

# Open chrome window, select raymond profile and open pages
# # Url1
chrome2 = subprocess.Popen([command3, "--profile-directory=Profile 1", "--window-size=800,600", "--new-window", url1])
# # Url2
chrome2 = subprocess.Popen([command3, "--profile-directory=Profile 1", "--window-size=800,600", url2])
# # Url3
chrome2 = subprocess.Popen([command3, "--profile-directory=Profile 1", "--window-size=800,600", url3])
# # Url4
# # chrome2 = subprocess.Popen([command3, "--profile-directory=Profile 1", "--window-size=800,600", url4])

# Start subprocesses command2, Logitech Gaming Software
# I use the G13 for coding these days. I have a profile for each language I use.
g13 = subprocess.Popen([command2])

