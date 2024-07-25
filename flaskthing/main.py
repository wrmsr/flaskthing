from flask import Blueprint
from flask import render_template
from flask_login import current_user
from flask_login import login_required


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
