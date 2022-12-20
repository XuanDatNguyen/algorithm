import requests
from settings import USERNAME, PASSWORD, SHOP, ADMIN_ACCESS_TOKEN

base_url = F"https://{USERNAME}:{PASSWORD}@{SHOP}.myshopify.com/admin/api/2022-10/"
headers = {'Content-Type': 'application/json',
           'X-Shopify-Access-Token': ADMIN_ACCESS_TOKEN}


def get_products():
    url = F"{base_url}products.json"
    res = requests.get(url, headers=headers)
    return res.text


def create_product(data):
    url = F"{base_url}products.json"
    res = requests.post(url, json=data, headers=headers)
    return res.text


def update_product(product_id, data):
    url = F"{base_url}/products/{product_id}.json"
    res = requests.put(url, headers=headers, json=data)
    return res.text


def delete_product(product_id):
    url = F"{base_url}/products/{product_id}.json"
    res = requests.delete(url, headers=headers)
    return res.status_code


# print(delete_product(8078773420305))8078790820113
# print(get_products())
data = {"product": {"title": "Test product"}}
print(create_product(data))
# print(update_product(8078790820113, data))
