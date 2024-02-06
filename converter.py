from PIL import Image
from sys import argv, exit
from os import listdir, path, mkdir

try:
    src, dest = argv[1], argv[2]
except IndexError:
    exit("Please specify source directory followed by destination directory...")

if not path.exists(dest):
    mkdir(dest)

try:
    for file in listdir(src):
        img = Image.open(path.join(src,file))
        img.save(path.join(dest, "".join([path.splitext(file)[0], ".png"])), "png")
except FileNotFoundError:
    exit("Please ensure source directory exists...")


