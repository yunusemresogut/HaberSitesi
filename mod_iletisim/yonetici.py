from flask import Blueprint, render_template

mod_iletisim = Blueprint('iletisim', __name__)

@mod_iletisim.route('/hakkimizda')
def iletisimListe():
    return render_template('contact.html')