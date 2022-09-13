import json
import os
import random
import time

import requests

from faker import Faker


BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

fake = Faker()


def fake_phone_number():
    return fake.msisdn()[:10]


def fake_weight():
    return random.randint(1, 1000)


def fake_price():
    return random.randint(1, 100000)


CUSTOMER_IDS = []
PRODUCT_IDS = []
STORE_IDS = []


CUSTOMER_FAKER_MAPPINGS = {
    'email': fake.email,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'street_address': fake.street_address,
    'city': fake.city,
    'state': fake.state_abbr,
    'zip_code': fake.postcode,
    'phone': fake_phone_number
}

CUSTOMER_UPDATABLE_FIELDS = ['first_name', 'last_name', 'street_address', 'city',
        'state', 'zip_code', 'phone']


PRODUCT_FAKER_MAPPINGS = {
    'sku': fake.ean8,
    'name': fake.catch_phrase,
    'description': fake.bs,
    'color': fake.color_name,
    'brand': fake.company,
    'weight': fake_weight,
    'price': fake_price
}

PRODUCT_UPDATABLE_FIELDS = ['name', 'description', 'color', 'brand', 'weight',
    'price']


STORE_FAKER_MAPPINGS = {
    'store_id': fake.ean8,
    'name': fake.street_name,
    'manager_name': fake.name,
    'street_address': fake.street_address,
    'city': fake.city,
    'state': fake.state_abbr,
    'zip_code': fake.postcode,
    'phone': fake_phone_number
}

STORE_UPDATABLE_FIELDS = ['name', 'manager_name', 'street_address', 'city', 
    'state', 'zip_code', 'phone']


##################################################################################


def create_new_entity(url_segment, entity_details, id_list):
    url = f'{BASE_URL}/api/v1/{url_segment}'
    request_body = json.dumps(entity_details)
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(url, data=request_body, headers=headers)
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


##################################################################################


def delete_entity(url_segment, id_list):
    if not id_list:
        return

    id_to_delete = random.choice(id_list)
    url = f'{BASE_URL}/api/v1/{url_segment}/{id_to_delete}'

    try:
        requests.delete(url)
        id_list.remove(id_to_delete)
    except Exception as err:
        print(err)


def delete_customer():
    delete_entity('customers', CUSTOMER_IDS)


def delete_product():
    delete_entity('products', PRODUCT_IDS)


def delete_store():
    delete_entity('stores', STORE_IDS)


##################################################################################

def update_entity(url_segment, updatable, faker_mappings, id_list):
    if not id_list:
        return

    field_to_update = random.choice(updatable)
    new_value_function = faker_mappings[field_to_update]
    new_value = new_value_function()

    id_to_update = random.choice(id_list)
    url = f'{BASE_URL}/api/v1/{url_segment}/{id_to_update}'
    request_body = json.dumps({field_to_update: new_value})
    headers = {'Content-type': 'application/json'}

    try:
        requests.put(url, data=request_body, headers=headers)
    except Exception as err:
        print(err)    


def update_customer():
    update_entity('customers', CUSTOMER_UPDATABLE_FIELDS, 
        CUSTOMER_FAKER_MAPPINGS, CUSTOMER_IDS)


def update_product():
    update_entity('products', PRODUCT_UPDATABLE_FIELDS, 
        PRODUCT_FAKER_MAPPINGS, PRODUCT_IDS)


def update_store():
    update_entity('stores', STORE_UPDATABLE_FIELDS,
        STORE_FAKER_MAPPINGS, STORE_IDS)



##################################################################################

def build_new_entity(mappings):
    return {k: v() for (k, v) in mappings.items() }


def build_new_customer():
    return build_new_entity(CUSTOMER_FAKER_MAPPINGS)


def build_new_product():
    return build_new_entity(PRODUCT_FAKER_MAPPINGS)


def build_new_store():
    return build_new_entity(STORE_FAKER_MAPPINGS)


CHANGE_METHODS = [
    create_new_customer,
    update_customer,
    delete_customer,
    create_new_product,
    update_product,
    delete_product,
    create_new_store,
    update_store,
    delete_store
]


def send_changes():
    while True:
        send_change()
        sleep_time = random.randint(1, 100) // 10   # Sleep from 0.1 - 10 s
        time.sleep(sleep_time)


def send_change():
    change_fuction = random.choice(CHANGE_METHODS)
    change_fuction()



if __name__ == '__main__':
    send_changes()
