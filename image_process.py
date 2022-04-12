from cv2 import cv2 as cv2 
import os


rootdir="/Users/chenguanshou/CODE/Gene_Dics_Design/main/static/data/"

filelist=os.listdir(rootdir)
list_images=[]
for image in filelist:
    if image.endswith(".png"):
        print(rootdir+image)
        img=cv2.imread(rootdir+image,cv2.IMREAD_COLOR)
        flip_H = cv2.flip(img, 1)
        cv2.imwrite("main/static/data/ori_"+image, flip_H,[cv2.IMWRITE_PNG_COMPRESSION, 5])
