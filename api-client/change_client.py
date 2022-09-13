import json
import os
import random
import time

import requests

from faker import Faker


BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')

fake = Faker()


def send_changes():
    while True:
        send_change()
        sleep_time = random.randint(1, 100) // 10   # Sleep from 0.1 - 10 s
        time.sleep(sleep_time)


def send_change():
    send_new_customer()


def send_new_customer():
    url = f'{BASE_URL}/api/v1/customers'
    requst_body = json.dumps(build_new_customer())
    headers = {'Content-type': 'application/json'}
    
    try:
        requests.post(url, data=requst_body, headers=headers)
    except Exception as err:
        print(err)


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


if __name__ == '__main__':
    send_changes()
