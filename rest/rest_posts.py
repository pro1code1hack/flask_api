import base64

from flask import request
from flask_restful import Resource

from app import db, api
from models.posts import User_post

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic
    #render_file = render_picture(data)

# sdelat tak, chtob kartinku mozha bilo zagruzhat v etu papku!


class Smoke(Resource):
    def get(self):
        return {'message':'OK'}, 200

class PostsList_Api(Resource):
    def get(self, uuid =None):
        if not uuid:
            posts = db.session.query(User_post).all()
            return [p.to_dict() for p in posts], 200
        post = db.session.query(User_post).filter_by(uuid = uuid).first()
        if not post:
            return '', 404
        return post.to_dict(), 200

    def post(self):
        post_json = request.json
        if not post_json:
            return {'message': "Wrong data"}, 400
        try:
            post = User_post(
                title = request.json['title'],
                author = request.json['author'],
                description= request.json['description'],
                rendered_data_of_pic = request.json['rendered_data_of_pic'],
                url = request.json['url']
            )
            db.session.add(post)
            db.session.commit()
        except ValueError:
            return {'message': "Wrong data"}, 400
        return "Created suc", 201
    def put(self, uuid):
        post_json = request.json
        if not post_json:
            return {'message': "Wrong data"}, 400
        try:
            db.session.query(User_post).filter_by(uuid= uuid).update(
                dict(
                    title=request.json['title'],
                    author=request.json['author'],
                    description=request.json['description'],
                    rendered_data_of_pic=request.json['rendered_data_of_pic'],
                    url=request.json['url']
                )
            )
            db.session.commit()
        except ValueError:
            return {'message': "Wrong data"}, 400
        return "Updated suc", 201

    def delete(self, uuid):
        post = db.session.query(User_post).filter_by(uuid=uuid).first()
        if not post:
            return {'message': "Wrong data"}, 400
        try:
            post = db.session.query(User_post).filter_by(uuid=uuid).first()
            db.session.delete(post)
            db.session.commit()
        except ValueError:
            return {'message': "Wrong data"}, 400
        return "Deleted suc", 201


api.add_resource(Smoke, '/smoke', strict_slashes = False)
api.add_resource(PostsList_Api, '/posts', strict_slashes = False)


