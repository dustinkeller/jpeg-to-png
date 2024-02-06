# jpeg-to-png
## Purpose
When editing photos, sometimes we want to convert to file formats that suit our needs best. This simple script can be run from the command line and allow you to automatically convert all JPEG images from a specified source directory to PNG images in a specified destination directory.

## Usage
Open the terminal, navigate to the directory containing this script, and run

```
python3 converter.py "/your/source/folder/" "/your/destination/folder/"
```

Note that the destination directory can either already exist or be created automatically using the script. 

## Dependencies
    - [PIL](https://github.com/python-pillow/Pillow)