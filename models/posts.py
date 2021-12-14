import base64
import uuid

from datetime import datetime as dt

from app import db



class User_post(db.Model):
    tablename = 'user_post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    posted_date = db.Column(db.String(20),)
    uuid = db.Column(db.String(36), unique=True)
    author = db.Column(db.Text)
    rendered_data_of_pic = db.Column(db.Text, nullable=False)      # here we are rendering the data!
    description = db.Column(db.String(750), nullable=False)
    url = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))      # relationships

    def __init__(self,title,author,description, rendered_data_of_pic, url):
        self.title = title
        self.posted_date = str(dt.now())
        self.description = description
        self.author = author
        self.uuid = str(uuid.uuid4())
        self.rendered_data_of_pic = rendered_data_of_pic
        self.url = url

    def __repr__(self):
        return f'Film {self.title, self.uuid, self.posted_date, self.description}'

    def to_dict(self):     # to serialize
        return {
            'title':self.title,
            'uuid':self.uuid,
            'posted_date': self.posted_date,
            'description': self.description,
            'author': self.author,
            'rendered_data_of_pic': self.rendered_data_of_pic,
            'url':self.url,
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=dt.now())
    updated_at = db.Column(db.DateTime, default=dt.now())
    posts = db.relationship('User_post', backref = "user")