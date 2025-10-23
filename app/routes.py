from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegisterForm
from flask_login import login_required, user_login_confirmed

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return redirect(url_for('main.register'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        return render_template("register.html", form=form, name=name)

    return render_template('register.html', form=form,name=name)