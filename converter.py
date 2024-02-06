from PIL import Image
from sys import argv, exit
from os import listdir, path, mkdir

try:
    src, dest = argv[1], argv[2]
except IndexError:
    exit("Please specify source directory followed by destination directory...")


try:
    input_images = listdir(src)

    if not path.exists(dest):
        mkdir(dest)
    
    for file in input_images:
        img = Image.open(path.join(src,file))
        output_path = path.join(dest, f"{path.splitext(file)[0]}.png")
        img.save(output_path, "png")
except FileNotFoundError:
    exit("Please ensure source directory or destination parent directory exists...")