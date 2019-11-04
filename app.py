# http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
'''
in python3 shell:
>>> from app import db
>>> db.create_all()
Boom, and there is your database. Now to create some users:

>>> from app import User
>>> admin = User(username='admin', email='admin@example.com')
>>> guest = User(username='guest', email='guest@example.com')
>>> guest2 = User(username='guest2', email='guest2@example.com')
But they are not yet in the database, so let’s make sure they are:

>>> db.session.add(admin)
>>> db.session.add(guest)
>>> db.session.add(guest2)
>>> db.session.commit()

'''


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI #'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def home():
    users = User.query.all()
    print(users)
    return render_template('home.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, port=8111)