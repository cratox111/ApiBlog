from flask import request, jsonify
from app.models.model_posts import Posts

def getPosts():
    posts = Posts.query.all()

    return jsonify([p.to_dict() for p in posts])

def getPost(id):
    post = Posts.query.get(id)

    if not post:
        return jsonify({'message':'not post'})
    
    return jsonify(post.to_dict())