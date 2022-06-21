from tkinter import Frame
from flask import render_template,Blueprint,Response,redirect,url_for,flash,request,flash
import os,json
from main import db
from base64 import b64encode
import base64
from cv2 import cv2

database=Blueprint('database',__name__)

def render_picture(data):

    render_pic = base64.b64encode(data).decode('ascii') 
    return render_pic

@database.route('/')
def home():

    return render_template('database/imgUpload.html')


@database.route('/upload', methods=['POST'])
def upload():

   file = request.files['inputFile']
   ##
   ##opencv read image and convert to bytes
   ##
   frame=cv2.imread("main/static/data/04-01-2022-14-08-35.png")
   _, img_encode = cv2.imencode('.png', frame)
   img_bytes=img_encode.tobytes()
   
   data = file.read()##type is bytes

   render_file = render_picture(data)
   render_file = render_picture(img_bytes)
   text = request.form['text']
   location = request.form['location']

#    newFile = FileContent(name=file.filename, data=data, 
#    rendered_data=render_file, text=text, location=location)
#    db.session.add(newFile)
#    db.session.commit() 
   flash(f'Pic {file.filename} uploaded Text: {text} Location: {location}')
   return render_template('database/showdata.html',data=render_file)
#    return render_template('upload.html')