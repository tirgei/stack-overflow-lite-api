from app.api.utils.validators import Validators
from app.api.v1.models.user_model import User
from flask import jsonify, Blueprint, request, json
from werkzeug.security import generate_password_hash

db = User()
validate = Validators()
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth.route('/register', methods=['POST'])
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

    return jsonify({"status": 201, "message": "user successfully created"}), 201
