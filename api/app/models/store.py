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