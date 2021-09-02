# from flask import render_template, flash, redirect, url_for, request, jsonify
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
# from app import app
# from app.models import User
#
#
# # Create a route to authenticate your users and return JWT Token. The
# # create_access_token() function is used to actually generate the JWT.
# @app.route('/token', methods=['POST'])
# def create_token():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     # Query your database for username and password
#     user = User.query.filter_by(username=username, password=password).first()
#     if user is None:
#         # the user was not found on the database
#         return jsonify({"msg": "Bad username or password"}), 401
#
#     # create a new token with the user id inside
#     access_token = create_access_token(identity=user.id)
#     return jsonify({"token": access_token, "user_id": user.id})
#
#
# # Protect a route with jwt_required, which will kick out requests
# # without a valid JWT present.
# @app.route('/protected', methods=['GET'])
# @jwt_required()
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user_id = get_jwt_identity()
#     user = User.filter.get(current_user_id)
#
#     return jsonify({'id': user.id, 'username': user.username}), 200
