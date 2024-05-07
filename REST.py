from flask import Flask, request, jsonify
from sqlserver import create_connection, add_product as db_add_product, remove_product as db_remove_product, update_product as db_update_product
app = Flask(__name__)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    db_add_product(name, price, quantity)
    return jsonify({'message': 'Product added successfully'}), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    quantity = data.get('quantity')
    db_update_product(product_id, name, price, quantity)
    return jsonify({'message': 'Product updated successfully'}), 200


@app.route('/products/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    db_remove_product(product_id)
    return jsonify({'message': 'Product removed successfully'}), 200

@app.route('/products', methods=['GET'])
def list_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Produtos')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    products_list = [{'ProdutoID': row[0], 'Nome': row[1], 'Preco': row[2], 'Quantidade': row[3]} for row in products]
    return jsonify(products_list), 200

if __name__ == '__main__':
    app.run(debug=True)
