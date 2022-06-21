from flask import render_template,Blueprint,Response
import os,json

from numpy import append

Dashboard=Blueprint('Dashboard',__name__)
@Dashboard.route('/home')
def home():
    return render_template('dashboard/homepage.html')

@Dashboard.route('/showdata')
def show_data():
    pjdir = os.path.abspath(os.path.dirname(__file__))
    rootdir=""
    for dir in pjdir.split("/")[:-1]:
        rootdir+=dir+"/"
    data_dir=rootdir+"/static/data"
    filelist=os.listdir(data_dir)
    list_images=[]
    for image in filelist:
        if image.endswith(".png"):
            list_images.append({"name":image,"src":"data/"+image})
    print(list_images[1]["src"])
    return render_template('dashboard/showdata.html',images=list_images)

@Dashboard.route('/accountManager')
def accountManager():
    return "issuperuser"