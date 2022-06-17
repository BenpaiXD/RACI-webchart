from flask import Blueprint, render_template, flash
from flask import request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Log out</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4 or not email.__contains__('@') or not email.__contains__('.'):
            flash('Invalid Email address', category='error')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7: 
            flash('Password must be at least 7 characters', category='error')
        else:
            flash('Account Created', category='success')

    return render_template("sign_up.html")
