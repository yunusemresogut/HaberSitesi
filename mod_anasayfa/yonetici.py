from flask import Blueprint, render_template

mod_anasayfa = Blueprint('anasayfa', __name__)

@mod_anasayfa.route('/home')
def ansayfaHome():
    return render_template('index.html')