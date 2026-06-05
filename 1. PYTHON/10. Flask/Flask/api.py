## put abd delete - HTTP verbs
## Working with API's--JSON

from flask import Flask,jsonify,request
app = Flask(__name__)

## Initial Data in my to do list
items = [
    {"id":1,"name":"Item 1","desc":"This is item 1"},
    {"id":2,"name":"Item 2","desc":"This is item 2"},
    {"id":3,"name":"Item 3","desc":"This is item 3"}
]

@app.route('/')
def home():
    return "Welcome to the Sample TO DO List App"

## GET : Retrieve all the items
@app.route('/items',methods=['GET'])
def getItem():
    return jsonify(items)

## GET : retrieve specific items by id
@app.route('/items/<int:item_id>',methods=['GET'])
def getItems(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)
    
## POST : create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json :
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "desc":request.json['desc']
    }
    items.append(new_item)
    return jsonify(new_item)

## PUT : Updating an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['desc'] = request.json.get('desc', item['desc'])
    return jsonify(item)

## DELETE : delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result":"Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)