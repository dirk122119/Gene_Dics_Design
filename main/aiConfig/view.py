from click import argument
from flask import render_template,Blueprint,Response,request
import os,glob,json

from numpy import append
from flask import flash

aiConfig=Blueprint('aiConfig',__name__)
@aiConfig.route('/home',methods=['GET', 'POST'])
def home():
    argument={}
    pjdir = os.path.abspath(os.path.dirname(__file__))
    test=pjdir[:-9]+"/static/data"
    get_model=glob.glob(os.path.join(test, "*.png"))
    argument["modelList"]=get_model
    if(request.method=="POST"):
        print(request.form["IOU"])
        flash(request.form["IOU"])
        import subprocess
        subprocess.run('ls',shell=True)

    return render_template('aiConfig/config.html',test=argument)

