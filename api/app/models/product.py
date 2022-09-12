from .. import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    color = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    price = db.Column(db.Numeric(5,2))


    def __repr__():
        return f'Product: {sku}'