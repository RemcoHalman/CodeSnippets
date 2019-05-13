import os
import sys
import logging
from os.path import join
from PIL import Image, ImageEnhance

# Dependancies
# Pillow 5.3.0

# Adding a "filename" argv
scriptrunning = sys.argv[0]

# Basic config + auto filename log
logging.basicConfig(filename=f"{scriptrunning}.log", level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : script_line(%(lineno)d) : %(message)s ')


def FolderSelectAndRun():
    batch(
        "input_folder!!!!",
        "output_folder!!!!",
        "watermark!!!!"
    )


basewidth = 2048

def batch(infolder, outfolder, watermark):
    mark = Image.open(watermark)
    count = 0
    for root, dirs, files in os.walk(infolder):
        for name in files:
            try:
                count += 1
                im = Image.open(join(root, name))

                # New image in the making
                layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
                position = (im.size[0] - (mark.size[0] + 50),
                            im.size[1] - (mark.size[1] + 50))
                layer.paste(mark, position)
                new_image = Image.composite(layer, im, layer)

                # Resize in perspective
                wpercent = (basewidth / float(im.size[0]))
                hsize = int((float(new_image.size[1]) * float(wpercent)))
                smaller_new_image = new_image.resize(
                    (basewidth, hsize), Image.ANTIALIAS)

                # Save new smaller image
                smaller_new_image.save(
                    join(outfolder, ('with-logo_' + name)), 'jpeg')

            except Exception as error:
                # Debug line while making changes
                # print('Caught this error: ' + repr(error))
                logging.error('Caught this error: ' + repr(error))
    logging.info(f"Images processed {count}")


if __name__ == '__main__':
    FolderSelectAndRun()
