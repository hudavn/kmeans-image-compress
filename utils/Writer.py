from unittest import result
import numpy as np
import matplotlib.pyplot as plt


def CreateNewImage(pixels, k, filetype, filename):
    resultFile = f'output/modified-{k}-colors-{filename}.{filetype}'
    
    plt.imsave(resultFile, pixels.astype('uint8'))

    print("--- [INFO] Finish! Created ", resultFile)
    if filetype == 'pdf':
        print("--- [INFO] Note: Open file with explorer/browser support this format")
    
        