from flask import Blueprint, render_template

mod_admin = Blueprint('admin', __name__)

@mod_admin.route('/login')
def adminLogin():
    return render_template('login.html')