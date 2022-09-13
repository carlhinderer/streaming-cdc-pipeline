from flask import jsonify, request

from . import api
from .. import db
from ..models.product import Product


@api.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify({ 'products': [p.to_json() for p in products] })


@api.route('/products/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_json())


@api.route('/products', methods=['POST'])
def new_product():
    product = Product.from_json(request.json)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_json()), 201


@api.route('/products/<int:id>', methods=['PUT'])
def edit_product(id):
    product = Product.query.get_or_404(id)

    product.sku = request.json.get('sku', product.sku)
    product.name = request.json.get('name', product.name)
    product.description = request.json.get('description', product.description)
    product.color = request.json.get('color', product.color)
    product.brand = request.json.get('brand', product.brand)
    product.weight = request.json.get('weight', product.weight)
    product.price = request.json.get('price', product.price)
    
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_json())
    

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify(product.to_json()), 204
