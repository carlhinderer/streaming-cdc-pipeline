import os

from app import create_app, db

from app.models.customer import Customer
from app.models.product import Product
from app.models.store import Store



app = create_app(os.getenv('FLASK_CONFIG') or 'default')



@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Customer=Customer, Product=Product, Store=Store)