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
   from main.aiConfig.model import furnitureDatabase
   ##upload file way
   file = request.files['inputFile']
   data = file.read()##type is bytes
   render_file = render_picture(data)
   text = request.form['text']
   location = request.form['location']
   ##
   ##opencv read image and convert to bytes
   ##
   frame=cv2.imread("main/static/data/04-01-2022-14-08-35.png")
   _, img_encode = cv2.imencode('.png', frame)
   img_bytes=img_encode.tobytes()##type is bytes
   
   
   render_file = render_picture(img_bytes)

   new_furniture=furnitureDatabase(imgName="test",imgInputDate="12-34-56",imgInputFrom="ee",imgRendered_data=render_file,imgData=img_bytes)
   db.session.add(new_furniture)
   db.session.commit() 
#    newFile = FileContent(name=file.filename, data=data, 
#    rendered_data=render_file, text=text, location=location)
#    db.session.add(newFile)
#    db.session.commit() 
   data=furnitureDatabase.query.first()
   flash(f'Pic {file.filename} uploaded Text: {text} Location: {location}')
   return render_template('database/showdata.html',data=data.imgRendered_data)
#    return render_template('upload.html')