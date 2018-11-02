from datetime import timedelta
from flask import Flask 
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.secret_key = 'paco'
api= Api(app)


jwt = JWT(app, authenticate, identity)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///holi.db'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=9999999999)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def crate_tables():
    db.create_all()

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
db.init_app(app)

if __name__== "__main__":
    app.run(host='0.0.0.0')