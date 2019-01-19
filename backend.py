import flask
import simplejson as json
from json import JSONEncoder
from bson.json_util import dumps

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["items"]




app = flask.Flask(__name__)
app.config["DEBUG"] = True


class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


class Item:
    def __init__(self, item_position, picture, name):
        self.item_position = item_position
        self.picture = picture
        self.name = name


class ClothingManager:
    clothing_item = {}
    item_number = 0
    item_position = ""

    def add(self, name, position, pic):

        self.item_number = self.item_number + 1
        item = Item(position, pic, name)
        add_to_db(item)
        self.clothing_item[self.item_number] = item
        add_to_db(item)

    def get_all_items(self):
        # return self.clothing_item
        return mycol.find()


def add_to_db(item):
    mydict = {"name": item.name, "position": item.item_position, "picture": item.picture}
    x = mycol.insert_one(mydict)


def create_item(pos, pic):
    return Item(pos, pic)


def add_item(pos, pic):
    return Item(pos, pic)


@app.route('/wardrobe', methods=['GET'])
def home():
    c1 = ClothingManager()
    c1.add("pant", "bottom", "random")
    c1.add("pant", "bottom", "random")
    c1.add("pant", "bottom", "random")
    c1.add("shirt", "top", "random")
    c1.add("shirt", "top", "random")
    c1.add("shirt", "top", "random")
    c1.add("shirt", "top", "random")
    c1.add("hat", "head", "random")
    c1.add("hat", "head", "random")
    c1.add("hat", "head", "random")
    c1.add("hat", "head", "random")
    c1.add("boot", "shoes", "random")
    c1.add("boot", "shoes", "random")
    c1.add("boot", "shoes", "random")
    c1.add("boot", "shoes", "random")

    # return MyEncoder().encode(c1.get_all_items())
    return dumps(c1.get_all_items())


@app.route('/test', methods=['GET'])
def home1():
    return "test"


app.run()
