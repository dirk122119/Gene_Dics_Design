from flask import Flask,redirect,url_for,flash
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin,AdminIndexView,expose
from flask_admin.contrib.sqla import ModelView

app=Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = 'login'
login.init_app(app)

@login.user_loader
def load_user(user_id):
    from  main.userInfo.model import UserRegister
    return UserRegister.query.get(int(user_id))

db = SQLAlchemy(app)
migrate=Migrate(app,db)

@app.route("/")
def hello():
    return redirect(url_for('Dashboard.home'))

from main.dashboard.view import Dashboard
from main.camera.view import Camera
from main.userInfo.view import userInfo
from main.aiConfig.view import aiConfig
from main.database.view import database

app.register_blueprint(Dashboard,url_prefix='/dashboard')
app.register_blueprint(Camera,url_prefix='/camera')
app.register_blueprint(userInfo,url_prefix='/userInfo')
app.register_blueprint(aiConfig,url_prefix='/aiConfig')
app.register_blueprint(database,url_prefix='/database')
from main.userInfo.model import UserRegister
from main.aiConfig.model import furnitureDatabase

class MyModeView(ModelView):
    """
    判斷是否為superuser
    """
    def is_accessible(self):
        return current_user.superuser
   




class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.superuser

    def inaccessible_callback(self, name, **kwargs):
        flash("沒有權限")
        return redirect(url_for('userInfo.login'))

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):

        return redirect("../admin/userregister")
admin=Admin(app,index_view=MyAdminIndexView(),name="後台")
admin.add_view(MyModeView(UserRegister,db.session,name="帳號管理"))
admin.add_view(MyModeView(furnitureDatabase,db.session,name="資料庫"))