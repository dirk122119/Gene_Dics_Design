from main import db,bcrypt
from main import login
class furnitureDatabase(db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = u'furniture'
    id = db.Column(db.Integer, primary_key=True)
    imgName = db.Column(db.String(80), unique=True, nullable=False)
    imgInputDate=db.Column(db.String(80), unique=False, nullable=False)
    imgInputFrom=db.Column(db.String(80), unique=False, nullable=False)
    imgRendered_data=db.Column(db.Text, nullable=False)#Data to render the pic in browser
    imgData=db.Column(db.LargeBinary, nullable=False) #Actual data, needed for Download

    


