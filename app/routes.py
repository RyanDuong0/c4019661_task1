from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegisterForm, LoginForm, LogoutForm
from flask_login import login_required, user_login_confirmed

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return redirect(url_for('main.register'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == "admin" and password == "password123":
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html", form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    name = None
    if form.validate_on_submit():
        name = form.username.data
        return render_template("register.html", form=form, name=name)

    return render_template('register.html', form=form,name=name)

@main.route('/dashboard')
@login_required
def dashboard():
    form = LogoutForm()
    user = request.args.get('user', 'Guest')
    return render_template('dashboard.html', user=user, form=form)