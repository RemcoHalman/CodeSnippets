import os
from PIL import Image

file_path = os.getcwd()
list = os.listdir(file_path)

try:
    basewidth = 2048
    for file in list:
        if file.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(file)
            if img.height > basewidth or img.width > basewidth:
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                img.save("smal-" + file)
        else:
            print("no files found")
except Exception as e:
    raise
