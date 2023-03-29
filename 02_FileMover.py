from PIL import Image
import os

downloadsFolder = r"C:/Users/Cómputo/Desktop/Python/FDownloads/"
files = os.listdir(downloadsFolder)

audioFolder = r"C:/Users/Cómputo/Desktop/Python/FDownloads/Audio/"
videoFolder = r"C:/Users/Cómputo/Desktop/Python/FDownloads/Video/"
picturesFolder= r"C:/Users/Cómputo/Desktop/Python/FDownloads/Pictures/"

if __name__ == "__main__":
    for filename in files:
        name,extension = os.path.splitext(downloadsFolder + filename)
        if extension in [".jpg", ".png", ".jpeg"]:
            pictures = Image.open(downloadsFolder + filename)
            pictures.save(downloadsFolder + 'compressed_' + filename, optimize = True, quality = 60)
            os.remove(downloadsFolder + filename)

    if extension in [".mp3"]:
        os.rename(downloadsFolder + filename, audioFolder + filename)

    if extension in [".mp4"]:
        os.rename(downloadsFolder + filename, videoFolder + filename)
