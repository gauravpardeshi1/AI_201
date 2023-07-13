import pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

dishes_filename = 'dishes.pickle'
orders_filename = 'orders.pickle'

dishes = load_data(dishes_filename)
orders = load_data(orders_filename)
order_id = 1

@app.route('/dishes', methods=['POST'])
def create_dish():
    new_dish = {
        'id': len(dishes) + 1,
        'name': request.json['name'],
        'price': request.json['price'],
        'availability': request.json['availability']
    }
    dishes.append(new_dish)
    save_data(dishes, dishes_filename)
    return jsonify(new_dish), 201

@app.route('/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes)

@app.route('/dishes/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish:
        return jsonify(dish)
    return jsonify({'message': 'Dish not found'}), 404

@app.route('/dishes/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish:
        dish['name'] = request.json.get('name', dish['name'])
        dish['price'] = request.json.get('price', dish['price'])
        dish['availability'] = request.json.get('availability', dish['availability'])
        save_data(dishes, dishes_filename)
        return jsonify(dish)
    return jsonify({'message': 'Dish not found'}), 404

@app.route('/dishes/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
    if dish:
        dishes.remove(dish)
        save_data(dishes, dishes_filename)
        return jsonify({'message': 'Dish deleted'})
    return jsonify({'message': 'Dish not found'}), 404

@app.route('/orders', methods=['GET'])
def get_order():
    return jsonify(orders)



@app.route('/orders', methods=['POST'])
def place_order():
    customer_name = request.json['customer_name']
    dish_ids = request.json['dish_ids']

    # Check if each dish is available
    available_dishes = []
    unavailable_dishes = []
    for dish_id in dish_ids:
        dish = next((dish for dish in dishes if dish['id'] == dish_id), None)
        if dish and dish['availability']:
            available_dishes.append(dish)
        else:
            unavailable_dishes.append(dish_id)

    if unavailable_dishes:
        return jsonify({'message': 'The following dish IDs are unavailable: {}'.format(unavailable_dishes)}), 400

    # Process the order
    global order_id
    order = {
        'order_id': order_id,
        'customer_name': customer_name,
        'dishes': available_dishes,
        'status': 'received'
    }
    orders.append(order)
    order_id += 1
    save_data(orders, orders_filename)
    return jsonify(order), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = next((order for order in orders if order['order_id'] == order_id), None)
    if order:
        new_status = request.json.get('status')
        if new_status:
            order['status'] = new_status
            save_data(orders, orders_filename)
            return jsonify(order)
        else:
            return jsonify({'message': 'No status provided'}), 400
    return jsonify({'message': 'Order not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)



























