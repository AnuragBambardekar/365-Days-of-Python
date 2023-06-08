from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Smith", "age": 30},
]

# GET request - Retrieve all items
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

# GET request - Retrieve a single item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# POST request - Create a new item
@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = {
        'id': data[-1]['id'] + 1,
        'name': request.json['name'],
        'age': request.json['age']
    }
    data.append(new_item)
    return jsonify(new_item), 201

# PUT request - Update an existing item by ID
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        item['name'] = request.json.get('name', item['name'])
        item['age'] = request.json.get('age', item['age'])
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# DELETE request - Delete an item by ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        data.remove(item)
        return jsonify({'message': 'Item deleted'})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run()
