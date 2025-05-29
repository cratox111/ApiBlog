from flask import jsonify, request
from app.models.model_user import Users
from app.models.model_posts import Posts
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

def registerUser():
    # Optiene los datos enviados por el cliente
    inputData = request.get_json()
    
    # Accede a los datos enviados por el cliente y los gaurda en distintas variables
    name = inputData.get('name')
    username = inputData.get('username')
    email = inputData.get('email')
    password = inputData.get('password')

    # Hace la pregunta ¿Los campos estan vacios? en caso que si manda un error
    if not name or not username or not email or not password:
        return jsonify({'message': 'data is missing'}), 400
    
    # Hace la pregunta ¿Ya existen el username y email? en caso que si manda un error
    if Users.query.filter_by(username=username).first() or Users.query.filter_by(email=email).first():
        return jsonify({'message': 'data already exists'}), 400
    
    # Hashea la contraseña gracias la funcion generate_password_hash que la importa de werkzeug.segurity
    passwordHash = generate_password_hash(password, method='pbkdf2:sha256')

    # Crea un objeto de la clase Users y rellena los parametros con los datos que ha enviado el cliente
    new_user = Users(name=name, username=username, email=email, password=passwordHash, rol='user')

    # Añade y guarda los datos en la DB
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'created user'}), 200
    

def loginUser():
    inputData = request.get_json()

    username = inputData.get('username')
    password = inputData.get('password')

    user = Users.query.filter_by(username=username).first()

    if not user:
       return jsonify({'messsage': 'user does not exist'}), 401
    
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'incorrect password'}), 401
    
    access_token = create_access_token(identity={'userid':user.id, 'username':user.name})

    return jsonify({
        'message': 'Login successful',
        'access_token': access_token
    }), 200

def ReadUser(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'user does not exist'})

    return jsonify(user.to_dict())
    
    
def UpdateUser(id):
    user = Users.query.get(id)
    inputData = request.get_json()
    
    if not user:
        return jsonify({'massage': 'user does not exist'})

    user.name = inputData.get('name', user.name)
    user.username = inputData.get('username', user.username)
    user.email = inputData.get('email', user.email)
    user.password = inputData.get('password', user.password)
    user.rol = inputData.get('rol', user.rol)

    db.session.commit()



def DeleteteUser(id):
    user = Users.query.get(id)

    if not user:
        return jsonify({'message': 'user does not exist'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'user delete'})

@jwt_required()
def createPost():
    input_data = request.get_json()
    identify = get_jwt_identity()

    user_id = identify['userid']
    user_create = identify['username']
    title = input_data.get('title')
    body = input_data.get('body')

    if not user_create or not title or not body:
        return jsonify({'message':'data is missing'})

    new_post = Posts(user_create=user_create, title=title, body=body)

    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message':'create post'})


