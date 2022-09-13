from flask import jsonify, request

from . import api
from .. import db
from ..models.store import Store


@api.route('/stores')
def get_stores():
    stores = Store.query.all()
    return jsonify({ 'stores': [s.to_json() for s in stores] })


@api.route('/stores/<int:id>')
def get_store(id):
    store = Store.query.get_or_404(id)
    return jsonify(store.to_json())


@api.route('/stores', methods=['POST'])
def new_store():
    store = Store.from_json(request.json)
    db.session.add(store)
    db.session.commit()
    return jsonify(store.to_json()), 201


@api.route('/stores/<int:id>', methods=['PUT'])
def edit_store(id):
    store = Store.query.get_or_404(id)

    store.store_id = request.json.get('store_id', store.store_id)
    store.name = request.json.get('name', store.name)
    store.manager_name = request.json.get('manager_name', store.manager_name)
    store.street_address = request.json.get('street_address', store.street_address)
    store.city = request.json.get('city', store.city)
    store.state = request.json.get('state', store.state)
    store.zip_code = request.json.get('zip_code', store.zip_code)
    store.phone = request.json.get('store', store.phone)
    
    db.session.add(store)
    db.session.commit()
    return jsonify(store.to_json())
    

@api.route('/stores/<int:id>', methods=['DELETE'])
def delete_store(id):
    store = Store.query.get_or_404(id)
    db.session.delete(store)
    db.session.commit()
    return jsonify(store.to_json()), 204
