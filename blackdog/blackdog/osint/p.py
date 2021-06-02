import glob 
from os import chdir,system
a = glob.glob("*")
for i in a:
    try:
        chdir(i)
        system("touch __init__.py")
        chdir("../")
    except NotADirectoryError:
        pass
