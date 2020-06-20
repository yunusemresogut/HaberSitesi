from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HaberFormu(FlaskForm):

    haberKodu = StringField(label="Haber Kodu", validators=[DataRequired(message="Haber Kodu boş geçilemez")])
    haberTuru = StringField(label="Haber Türü", validators=[DataRequired(message="Haber Türü boş geçilemez")])
    haberIcerik = StringField(label="Haber İçeriği", validators=[DataRequired(message="Haber İçeriği boş geçilemez")])
    kaydet = SubmitField(label="Kaydet")