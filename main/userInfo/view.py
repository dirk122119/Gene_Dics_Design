from flask import render_template,Blueprint,Response,redirect,url_for,flash
from flask_login import login_user, current_user, login_required,logout_user

import os,json
from main import db


userInfo=Blueprint('userInfo',__name__)

@userInfo.route('/')
def home():
    return "userInfo/home"

@userInfo.route('/register', methods=['GET','POST'])
def register():
    from main.userInfo.form import FormRegister
    from main.userInfo.model import UserRegister
    form = FormRegister()
    if form.is_submitted():
        user = UserRegister(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("Dashboard.home"))
    #return render_template('userInfo/register.html', form=form)

    return render_template('userInfo/register.html', form=form)

@userInfo.route('/login',methods=['GET', 'POST'])
def login():
    from main.userInfo.model import UserRegister
    from main.userInfo.form import FormLogin
    form = FormLogin()
    if form.is_submitted():
        #  當使用者按下login之後，先檢核帳號是否存在系統內。
        user = UserRegister.query.filter_by(username=form.username.data).first()
        if user:
            #  當使用者存在資料庫內再核對密碼是否正確。
            if user.check_password(form.password.data):
                login_user(user, form.remember_me.data)
                return redirect(url_for('Dashboard.home'))
            else:
                #  如果密碼驗證錯誤，就顯示錯誤訊息。
                flash('Wrong Email or Password')
        else:
            #  如果資料庫無此帳號，就顯示錯誤訊息。
            flash('Wrong Email or Password')
    return render_template('userInfo/login.html', form=form)

@userInfo.route('/logout')
def logout():
    logout_user()
    flash('Log Out See You.')
    return redirect(url_for('userInfo.login'))

@userInfo.route('/resetpassword', methods=['GET', 'POST'])
def reset_password():
    from main.userInfo.form import FormResetPasswordMail
    from main.userInfo.model import UserRegister
    form = FormResetPasswordMail()
    if form.is_submitted():
        if not UserRegister.query.filter_by(email=form.get_email.data).first():
            flash("找不到對應的email")
            return render_template('UserData/resetpasswordemail.html', form=form)
        else:
            user=UserRegister.query.filter_by(email=form.get_email.data).first()
            print("user----------->"+user.username)
            user.password = form.password.data
            db.session.commit()
            return redirect(url_for('userInfo.login'))
    return render_template('userInfo/resetpasswordemail.html', form=form)