from flask import Blueprint, render_template, url_for, redirect
from .model import *
from .formlar import HaberFormu
from flask_login import login_required

mod_haberler = Blueprint('haberler', __name__)

@mod_haberler.route('/liste')
@mod_haberler.route('/')
def haberlerListe():
    haber = Haberler.query.all()
    return render_template('adminpanel.html', veri=haber)

@mod_haberler.route("/ekle", methods=["GET", "POST"])
@login_required
def haberlerEkle():
    form = HaberFormu()
    if form.validate_on_submit():
        yeniHaber = Haberler()
        yeniHaber.haberKodu = form.haberKodu.data
        yeniHaber.haberTuru = form.haberTuru.data
        yeniHaber.haberIcerik = form.haberIcerik.data
        db.session.add(yeniHaber)
        db.session.commit()
        return redirect(url_for('haberler.haberlerListe'))
    return render_template('haberlerim/ekle.html', form=form, sayfa_baslik="Yeni Haber Ekle")