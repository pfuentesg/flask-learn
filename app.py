from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'paco'
api= Api(app)


jwt = JWT(app, authenticate, identity)

items =[]
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank!"
)
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {'item': item}, 200 if item else 404

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    
class Items(Resource):
    def get(self):
        return {'items:': items}

    def post(self):
        data = request.get_json()
        if  next(filter(lambda x: x['name']==data['name'], items), None):
            return{'message': 'item already exists'}, 400
        item = {'name': data['name'], 'price': data['price']}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=3030)