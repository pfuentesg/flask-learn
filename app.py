from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api= Api(app)

items =[]
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
            return {'item': None}, 404


class Items(Resource):
    def get(self):
        return {'items:': items}

    def post(self):
        data = request.get_json()
        item = {'name': data['name'], 'price': data['price']}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=3030)