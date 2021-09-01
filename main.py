from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)


# Create a route to authenticate your users and return JWT Token. The
# create_access_token() function is used to actually generate the JWT.
@app.route('/token', methods=['POST'])
def create_token():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # Query your database for username and password
    user = get_user(username=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401

    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user_id": user.id})


def get_user(username, password):
    if username == 'bird' and password == 'zxc123':
        return User(55)
    else:
        return None
