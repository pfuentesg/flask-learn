from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="This field cannot be left blank!"
)
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect("holi.db")
        cursor = connection.cursor()

        query = "SELECt * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {"message": "not found"}, 404


    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    @jwt_required()
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
    @jwt_required()
    def get(self):
        connection = sqlite3.connect("holi.db")
        cursor = connection.cursor()

        query = "SELECt * FROM items"
        result = cursor.execute(query)
        row = result.fetchone()
        connection.close()
        if row:
            return row
        return {"message": "not found"}, 404

    def post(self):
        data = Items.parser.parse_args()
        connection = sqlite3.connect('holi.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (data['name'], data['price']))

        return {"message':"Ok"}, 201