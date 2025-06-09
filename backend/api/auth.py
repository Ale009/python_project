<<<<<<< HEAD
from flask import Blueprint, current_app, request, jsonify
import json

auth_bp = Blueprint('auth', __name__)

# Carga el archivo JSON de base de datos
def load_db():
    # app.config['DATABASE_FILE']
    with open(current_app.config['DATABASE_FILE']) as f:
        return json.load(f)

def save_db(data):
    with open(current_app.config['DATABASE_FILE'], 'w') as f:
        json.dump(data, f, indent=2)

@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.json # Datos que vienen de postman (cliente)
    db = load_db() # Datos que estan en el servidor (DB)
    for user in db["users"]:
        if user['username'] == data["username"] and user["password"] == data["password"]:
            return jsonify({ 'mensaje': 'Login exitoso', 'user_id': user["id"] }), 200
        
    return jsonify({ 'error': 'Credenciales inválidas' }), 401

=======
from flask import Blueprint, request, jsonify
import json
import bcrypt
from db_sqlite import query_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.json # Datos que vienen de postman (cliente)
    #db = load_db() # Datos que estan en el servidor (DB)
    user = query_db(
        'SELECT * FROM users WHERE username = ?',
        (data['username'], ), one=True
    )

    if user:
        stored_hash = user['password']
        
        #Contraseña proporcionada por el usuario y el hash_bytes almacenado en la base de datos
        password_bytes = data['password'].encode('utf-8')
        stored_hash_bytes = stored_hash.encode('utf-8')
        
        # Verifica si la contraseña proporcionada coincide con el hash almacenado
        if bcrypt.checkpw(password_bytes, stored_hash_bytes):
            return jsonify({ 'mensaje': 'Login exitoso', 'user_id': user["id"] }), 200  

    return jsonify({ 'error': 'Credenciales inválidas' }), 401

""" 
>>>>>>> dev
@auth_bp.route('/register', methods=["POST"])
def register():
    data = request.json
    db = load_db()
    # Si existe un username en base de datos que sea igual al que viene en el request 
    if any(u["username"] == data["username"] for u in db["users"]):
        return jsonify({ 'error': 'Usuario ya existe' }), 400
    
    newUser = {
        'id': len(db['users']) + 1, # 3
        'username': data['username'],
        'password': data['password']
    }
    db["users"].append(newUser)
    save_db(db)
    return jsonify({ 'message:' 'Registrado correctamente' }), 201
<<<<<<< HEAD

@auth_bp.route('/users', methods=["GET"])
def get_users():
    db = load_db()
    return jsonify(db["users"]), 200
=======
"""

@auth_bp.route('/users', methods=["GET"])
def get_users():
    users = query_db("SELECT id, username FROM users")
    return jsonify([dict(user) for user in users]), 200
>>>>>>> dev
