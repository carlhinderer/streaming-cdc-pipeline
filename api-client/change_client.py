import json
import os
import random
import time

import requests

from faker import Faker


BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

fake = Faker()

CUSTOMER_IDS = []
PRODUCT_IDS = []
STORE_IDS = []


def send_changes():
    while True:
        send_change()
        sleep_time = random.randint(1, 100) // 10   # Sleep from 0.1 - 10 s
        time.sleep(sleep_time)


def send_change():
    create_new_customer()


def create_new_entity(url_segment, entity_details, id_list):
    url = f'{BASE_URL}/api/v1/{url_segment}'
    request_body = json.dumps(entity_details)
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(url, data=requst_body, headers=headers)
        new_record_id = response.json()['id']
        id_list.append(new_record_id)
    except Exception as err:
        print(err)


def create_new_customer():
    create_new_entity('customers', build_new_customer(), CUSTOMER_IDS)


def create_new_product():
    create_new_entity('products', build_new_product(), PRODUCT_IDS)


def create_new_store():
    create_new_entity('stores', build_new_store(), STORE_IDS)


def build_new_customer():
    customer = {
        'email': fake.email(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'street_address': fake.street_address(),
        'city': fake.city(),
        'state': fake.state_abbr(),
        'zip_code': fake.postcode(),
        'phone': fake.msisdn()[:10]
    }
    return customer


def build_new_product():
    product = {
        'sku': fake.ean8(),
        'name': fake.catch_phrase(),
        'description': fake.bs(),
        'color': fake.color_name(),
        'brand': fake.company(),
        'weight': random.randint(1, 1000),
        'price': fake.pricetag()[1:]
    }
    return product


def build_new_store():
    store = {
        'store_id': fake.ean8(),
        'name': fake.street_name(),
        'manager_name': fake.name(),
        'street_address': fake.street_address(),
        'city': fake.city(),
        'state': fake.state_abbr(),
        'zip_code': fake.postcode(),
        'phone': fake.msisdn()[:10]
    }
    return store


if __name__ == '__main__':
    send_changes()
