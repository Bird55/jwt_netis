from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from app import app
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# Create a route to authenticate your users and return JWT Token. The
# create_access_token() function is used to actually generate the JWT.
@app.route('/token', methods=['GET', 'POST'])
def create_token():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print('username = {}'.format(username))
        print('password = {}'.format(password))
        # Query your database for username and password
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            # the user was not found on the database
            return jsonify({"msg": "Bad username or password"}), 401

        # create a new token with the user id inside
        access_token = create_access_token(identity=user.id)
        return jsonify({"token": access_token, "user_id": user.id})
    return render_template('login.html', title='Sign In', form=form)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.filter.get(current_user_id)

    return jsonify({'id': user.id, 'username': user.username}), 200
