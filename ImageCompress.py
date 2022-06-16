import numpy as np

from utils import Writer, Reader, Clustering

if __name__ == "__main__":
    filePath, numColors, imageType = Reader.GetData()
    # filePath = "./data/image01.jpg"
    # numColors = 5
    # imageType = "png"

    filename = Reader.parseFileName(filePath)

    imageRawFlat, width, height = Reader.ReadImage(filePath)
    
    centers, labels = Clustering.kmeans(imageRawFlat, numColors)
    for i in range(len(labels)):
        imageRawFlat[i] = centers[labels[i]]

    Writer.CreateNewImage(imageRawFlat.reshape(height, width, -1), numColors, imageType, filename)

