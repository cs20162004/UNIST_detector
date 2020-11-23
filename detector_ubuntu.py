from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import glob
os.system
import PIL
import PIL.Image as Image
import sys

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

os.system('./darknet_ubuntu detector test model_single_class/mymodel.data model_single_class/yolov3-tiny.cfg backup/yolov3-tiny_15000.weights -dont_show ' + filename)

predicted_image = Image.open("predictions.jpg")
predicted_image.show()
