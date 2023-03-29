from PIL import Image
import os

downloadsFolder = r'C:/Users/Cómputo/Desktop/Python/FDownloads/'
files = os.listdir(downloadsFolder)

if __name__ == '__main__':
    for filename in files:
        name,extension = os.path.splitext(downloadsFolder+filename)
        if extension in ['.jpg','.png','.jpeg']:
            picture = Image.open(downloadsFolder+filename)
            picture.save(downloadsFolder+'Compressed_'+filename, optimize = True, quality = 60)