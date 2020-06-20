from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ÇOK GİZLİ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///haberler.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from mod_admin.yonetici import mod_admin
from mod_haberler.yonetici import mod_haberler
from mod_iletisim.yonetici import mod_iletisim
from mod_anasayfa.yonetici import mod_anasayfa

migrate = Migrate(app, db)

app.register_blueprint(mod_admin, url_prefix='/admin')
app.register_blueprint(mod_haberler, url_prefix='/haberler')
app.register_blueprint(mod_iletisim, url_prefix='/iletisim')
app.register_blueprint(mod_anasayfa, url_prefix='/anasayfa')

if __name__ == '__main__':
    app.run()
