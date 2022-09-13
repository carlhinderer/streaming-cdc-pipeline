from .. import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    manager_name = db.Column(db.String(255))
    street_address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.String(5))
    phone = db.Column(db.String(10))


    def __repr__():
        return f'Store: {store_id}'

    def to_json(self):
        json_store = {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'manager_name': self.manager_name,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone
        }
        return json_store

    @staticmethod
    def from_json(json_store):
        store_id = json_store.get('store_id')
        name = json_store.get('name')
        manager_name = json_store.get('manager_name')
        street_address = json_store.get('street_address')
        city = json_store.get('city')
        state = json_store.get('state')
        zip_code = json_store.get('zip_code')
        phone = json_store.get('phone')

        return Store(store_id=store_id,
                     name=name,
                     manager_name=manager_name,
                     street_address=street_address,
                     city=city,
                     state=state,
                     zip_code=zip_code,
                     phone=phone
                    )
