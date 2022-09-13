from flask import jsonify, request

from . import api
from .. import db
from ..models.customer import Customer


@api.route('/customers')
def get_customers():
    customers = Customer.query.all()
    return jsonify({ 'customers': [c.to_json() for c in customers] })


@api.route('/customers/<int:id>')
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_json())


@api.route('/customers', methods=['POST'])
def new_customer():
    breakpoint
    customer = Customer.from_json(request.json)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json()), 201


@api.route('/customers/<int:id>', methods=['PUT'])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)

    customer.email = request.json.get('email', customer.email)
    customer.first_name = request.json.get('first_name', customer.first_name)
    customer.last_name = request.json.get('last_name', customer.last_name)
    customer.street_address = request.json.get('street_address', customer.street_address)
    customer.city = request.json.get('city', customer.city)
    customer.state = request.json.get('state', customer.state)
    customer.zip_code = request.json.get('zip_code', customer.zip_code)
    customer.phone = request.json.get('phone', customer.phone)
    
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_json())
    

@api.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify(customer.to_json()), 204
