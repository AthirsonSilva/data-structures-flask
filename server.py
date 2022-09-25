import sqlite3
from flask import Flask, request, jsonify
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 0

db = SQLAlchemy(app)
now = datetime.now()

# configure sqlite3 to enforce foreign key contraints
@event.listens_for(Engine, 'connect')
def _set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute('PRAGMA foreign_keys=ON;')
            cursor.close()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=now)
    updated_at = db.Column(db.DateTime, default=now, onupdate=now)
    posts = db.relationship('BlogPost')


class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=now)
    updated_at = db.Column(db.DateTime, default=now, onupdate=now)
    date = db.Column(db.DateTime, default=now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# routes
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created'}), 200


@app.route('/user/descending_id', methods=['GET'])
def get_all_users_descending():
    pass


@app.route('/user/ascending_id', methods=['GET'])
def get_all_users_ascending():
    pass


@app.route('/user/<user_id>', methods=['GET'])
def get_one_user(user_id):
    pass


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass


@app.route('/blog_post/<user_id>', methods=['POST'])
def create_blog_post(post):
    pass

@app.route('/user/<user_id>', methods=['GET'])
def get_all_blog_posts(post):
    pass

@app.route('/blog_post/<blog_post_id>', methods=['GET'])
def get_one_blog_post(post):
    pass

@app.route('/blog_post/<blog_post_id>', methods=['DELETE'])
def delete_blog_post(post):
    pass

if __name__ == '__main__':
    app.run(debug=True)

