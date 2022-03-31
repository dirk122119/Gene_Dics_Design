from flask import redirect, render_template,Blueprint,Response,url_for,flash
from .camera import VideoCamera
from cv2 import cv2 as cv2 

def gen(camera):
    while True:
        frame,_ = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


video_stream = VideoCamera()

Camera=Blueprint('Camera',__name__)

@Camera.route('/video')
def video():
    return render_template('camera/camera.html')

@Camera.route('/video_feed')
def video_feed():
    print(type(gen(video_stream)))
    print(gen(video_stream))

    return Response(gen(video_stream),
    mimetype='multipart/x-mixed-replace; boundary=frame')

@Camera.route('/img_save')
def img_save():
    from datetime import datetime
    import pytz
    tw=pytz.timezone('Asia/Taipei')
    now = datetime.now().replace(tzinfo=tw) # current date and time
    str_time=now.strftime("%m-%d-%Y-%H-%M-%S")

    _,image=video_stream.get_frame()
    cv2.imwrite("main/static/data/"+str_time+".png", image,[cv2.IMWRITE_PNG_COMPRESSION, 5])
    flash("已取像")
    return redirect(url_for('Camera.video'))