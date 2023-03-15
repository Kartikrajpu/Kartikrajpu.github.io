import os

with open(os.path.expanduser("~/.bashrc"), "a") as file:
    file.write("echo 'Hello!'")
