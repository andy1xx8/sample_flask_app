
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()
DB_NAME = "database.db"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    orders = db.relationship('Order')
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="submitted")
    num_samples = db.Column(db.Integer)
    data = db.Column(db.String(10000))
    submit_date = db.Column(db.DateTime(timezone=True), default=func.now())
    done_date = db.Column(db.DateTime(timezone=True))
    note = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    samples = db.relationship('Sample')


class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="submitted")
    name = db.Column(db.String(20), nullable=False)
    submit_date = db.Column(db.DateTime(timezone=True), default=func.now())
    done_date = db.Column(db.DateTime(timezone=True))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
