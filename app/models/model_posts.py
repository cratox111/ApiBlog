from app import db

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_create = db.Column(db.Integer, db.foreign_key('users.id'))
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    public_date = db.Column(db.DateTime)

    comments = db.relationship('Comments', backreaf='post', lazy=True)

    def to_dict(self):
        return {
            'user_create':self.user_create,
            'title':self.title,
            'body':self.body,
        }