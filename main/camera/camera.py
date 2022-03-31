from cv2 import cv2 as cv2 

class VideoCamera(object):
    def __init__(self):
        #由opencv來獲取預設為0 裝置影像
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = self.video.read()
        flip_H = cv2.flip(frame, 1)
        ret, jpeg = cv2.imencode('.jpg', flip_H)

        return jpeg.tobytes(),flip_H