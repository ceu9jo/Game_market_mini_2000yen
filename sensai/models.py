from sensai import db
from sqlalchemy import Column, Integer, String

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    url = db.Column(db.String(32))
    price = db.Column(db.Integer)


def init():
    db.create_all()
