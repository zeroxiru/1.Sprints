
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Marshmallow
from datetime import datetime

# instantiate flask app
app = Flask(__name__)

# set configurations parameter
app.config['SQLAlCHEMY_DATABASE_URI'] = "sqlite:/// database.db"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

# INSTANTIATE DB object
db = SQLAlchemy(app)

# create marshmallow object

ma = Marshmallow(app)

# create database
class Todolist(db.Model):
    id = db.Columns(db.Integer, primary_key=True)
    name = db.Columns(db.String(200), nullable=False)
    description = db.Columns(db.String(500), nullable=False)
    completed = db.Columns(db.Boolean, default=False, nullable=False)
    date_created = db.Columns(db.DateTime, nullable=False, default=datetime.utcnow())


    def __repr__(self):
        return self.id

# create todolist schema
class TodolistSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'completed', 'date_created')

    # create instance of schemas
todolist_schema = TodolistSchema(many=False)
todolists_schema = TodolistSchema(many=True)





@app.route("/todolist")
def todo():
    return  jsonify({"Message": "Hello world, I am from Web API"})


if __name__ == "__main__":
    app.run(port=50000, debug=True)