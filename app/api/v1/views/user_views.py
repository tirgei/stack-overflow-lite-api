from app.api.utils.validators import Validators
from app.api.v1.models.user_model import User
from flask import jsonify, Blueprint, request, json
from werkzeug.security import generate_password_hash
from .. import version1 as v1

db = User()
validate = Validators()

@v1.route('/auth/register', methods=['POST'])
def register_user():
    ''' Endpoint to register user '''

    data = request.get_json()

    # Check if there's data in the request
    if not data:
        return jsonify({"status": 400, "message": "Please provide valid data"}), 400

    # Check if all values have been entered
    if not all(key in data for key in ["name", "email", "password"]):
        return jsonify({"status": 400, "message": "Please fill in all details"}), 400 

    email = data['email']
    password = data['password']

    # Validate provided email
    if not validate.valid_email(email):
        return jsonify({"status": 400, "message": "Invalid email"}), 400

    # Validate password
    if not validate.valid_password(password):
        return jsonify({"status": 400, "message": "Invalid password"}), 400

    #Check if user with email already exists
    if db.exists("email", email):
        return jsonify({"status": 400, 'message': "Email {} already exists".format(email)}), 400
    
    # Encrpyt password then save the user to the db
    data['password'] = generate_password_hash(password)
    db.save(data)

    return jsonify({"status": 201, "message": "User successfully created"}), 201

@v1.route('/users', methods=['GET'])
def fetch_users():
    ''' Endpoint to fetch all users '''

    users = db.all()

    if len(users) == 0:
        return jsonify({"status": 200, "data": users, "message": "No users found"}), 200
    else:
        return jsonify({"status": 200, "data": users}), 200

@v1.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    ''' Endpoint to update user information '''
    data = request.get_json()

    if not db.exists("id", id):
        return jsonify({"status":400, "message": "No user with id {} found".format(id)}), 400

    user = db.update(id, data)

    return jsonify({"status": 200, "message": "user successfully updated", "data": user})

@v1.route('/users/<int:id>', methods=['DELETE'])
def delete_account(id):
    ''' Endpoint to delete account '''

    user = db.delete(id)

    if user:
        return jsonify({"status": 200, "message" : "User successfully deleted"}), 200
    else :
        return jsonify({"status": 400, "message" : "No user with id {} found".format(id)}), 400