import numpy as np
import matplotlib.pyplot as plt


def CreateNewImage(pixels, k, filetype, filename):
    resultFile = f'output/modified-{k}-colors-{filename}.{filetype}'
    print("--- [INFO] Finish! Created ", resultFile)
    plt.imsave(resultFile, pixels.astype('uint8'))
    
        