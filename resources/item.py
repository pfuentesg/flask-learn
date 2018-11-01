from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank!"
)
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "not found"}, 404

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'messaje': 'item deleted'}
        return {'error': 'error removing item'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(data['name'], data['price'])

            items.append(item)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()

    
class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank!"
)
    parser.add_argument('name',
    required=True,
    help="This field cannot be left blank!"
)
    def get(self):
        items = ItemModel.find_all()
        if items:
            return items
        return {"message": "not found"}, 404

    def post(self):
        data = Items.parser.parse_args()
        if ItemModel.find_by_name(data['name']):
            return {"message": "item already exists"}, 400

        item = ItemModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return item.json(), 201