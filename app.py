from flask import (Flask, request)
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<Player %r>' % self.id

# Создание базы данных внутри контекста приложения
with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            db.session.add(Player(name='dima'))
            db.session.commit()
        except:
            print('error')
        return 'POST'
    else:
        try:
            res = Player.query.order_by(Player.name).all()
            
            print(res[2].name)
        except:
            print('error')
        return 'GET'
