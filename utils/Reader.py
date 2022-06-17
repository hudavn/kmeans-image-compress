from PIL import Image
import numpy as np
import os.path

def GetData():
    filePath = input("File path: ")

    if not os.path.exists(filePath):
        print("--- [ERROR] File path is not exist")
        exit()

    k = int(input("Compress to (number of colors): "))
    
    imageType = input("Image type (png, jpg, jpeg, pdf): ")
    if imageType not in ["png", "jpg", "jpeg", "pdf"]:
        print("--- [ERROR] Image type is invalid")
        exit()

    return filePath, k, imageType


def parseFileName(path): return ''.join(path.split('/')[-1].split('.')[:-1])


def ReadImage(file):
    im = Image.open(file)
    width, height = im.size
    return np.array(im.getdata()), width, height