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
    price = db.Column(db.Integer)

    def __repr__():
        return f'Product: {sku}'

    def to_json(self):
        json_product = {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'description': self.description,
            'color': self.color,
            'brand': self.brand,
            'weight': self.weight,
            'price': self.price
        }
        return json_product

    @staticmethod
    def from_json(json_product):
        sku = json_product.get('sku')
        name = json_product.get('name')
        description = json_product.get('description')
        color = json_product.get('color')
        brand = json_product.get('brand')
        weight = json_product.get('weight')
        price = json_product.get('price')

        return Product(sku=sku,
                       name=name,
                       description=description,
                       color=color,
                       brand=brand,
                       weight=weight,
                       price=price
                      )
