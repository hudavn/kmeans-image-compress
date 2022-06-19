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
    
    print()
    return filePath, k, imageType


def parseFileName(path): return ''.join(path.split('/')[-1].split('.')[:-1])


def ReadImage(file):
    im = Image.open(file)
    width, height = im.size
    rawData = list(im.getdata())

    print(f"--- [INFO] {file.split('/')[-1]} - {len(rawData)} pixels - {len(set(rawData))} colors")

    return np.array(rawData), width, height