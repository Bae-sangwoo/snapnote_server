import glob
from PIL import Image
import os

target_dir = os.path.join(r'C:\VSCODE\django\snapnote_django\snapnote', '*')
target_dir2 = os.path.join(r'C:\VSCODE\django\snapnote_django\snapnote\media\files\pdfs', '*')
files_jpg = glob.glob(target_dir + '*.jpg')
files_pdf = glob.glob(target_dir2 + '*.pdf')
cnt = len(files_jpg)
cnt2 = len(files_pdf)
halfcnt = cnt//2



def mergeImg():
    for i in range(halfcnt):
        im1 = Image.open(files_jpg[i])
        im2 = Image.open(files_jpg[i + halfcnt])
        blended = Image.blend(im1, im2, alpha=0.5)
        blended.save(r'C:\\VSCODE\\django\\snapnote_django\\snapnote\\blend\\merged' + str(i) + ".jpg")

def cleanDir():
    for i in range(cnt):
        if os.path.isfile(files_jpg[i]):
            os.remove(files_jpg[i])

def removepdf(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)

def cleanpdfDir():
    for i in range(cnt2):
        if os.path.isfile(files_pdf[i]):
            os.remove(files_pdf[i])


