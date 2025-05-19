from app import db

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.foreign_key('users.id'))
    post_id = db.Column(db.Integer, db.foreign_key('posts.id'))
    body = db.Column(db.Text)
    public_date = db.Column(db.DateTime)


