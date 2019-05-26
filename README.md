# Code Snippets

---

###### Setup for mac Terminal (TerminalSettings/)

###### Setup for NeuronPi PLC Terminal (TerminalSettings/)

---

#### Small Scripts

- `folder_creation.py`
  - Makes a current year folder and subfolders for all months. In working _directory_
- `resize_all_images.py`
  - Copy's all images and resizes them to set basewidth in script.
- `watermark.py`
  - Set a watermark in bottom right corner(dont make your watermark to big)
- `ui_converter.py`
  - Converting QtDesigner UI file to .py file. Place and use in the same directory as the `.ui` file

---

#### Batch adding watermark for images (watermark.py)
###### Free to use But use it at your own risk!
- Logging in the same location as the python script
- Paths to set:
  - Input Folder
  - Output Folder
  - Watermark (Tested working with .png)
    - Watermark will be placed in the bottom right corner
- Optional: Image is auto resized to 2048px width. Change this to desired width
