from app import db

"""Crea el modelo Users el cual tiene dos relaciones (post y commets) de uno a muchos"""
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    rol = db.Column(db.String(100))

    # Crea una relacion con la tabla Posts y crea la propiedad author en la tabla antes mencionada
    posts = db.relationship('Posts', backref='author', lazy=True)
    # Crea una relacion con la tabla Comments y crea la propiedad commenter en la tabla antes mencionada
    comments = db.relationship('Comments', backref='commenter', lazy=True)

    # Crea una funcion la cual convierte todo los datos a un diccionario y lo retorna#
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'rol': self.rol,
            'posts': [post.id for post in self.posts],
            'commets': [comment.id for comment in self.commets]
        }