from .. import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    street_address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.String(5))
    phone = db.Column(db.String(10))

    def __repr__(self):
        return f'Customer: {email}'

    def to_json(self):
        json_customer = {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'phone': self.phone
        }
        return json_customer

    @staticmethod
    def from_json(json_customer):
        email = json_customer.get('email')
        first_name = json_customer.get('first_name')
        last_name = json_customer.get('last_name')
        street_address = json_customer.get('street_address')
        city = json_customer.get('city')
        state = json_customer.get('state')
        zip_code = json_customer.get('zip_code')
        phone = json_customer.get('phone')

        return Customer(email=email,
                        first_name=first_name,
                        last_name=last_name,
                        street_address=street_address,
                        city=city,
                        state=state,
                        zip_code=zip_code,
                        phone=phone
                        )
