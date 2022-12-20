import requests
from settings import USERNAME, PASSWORD, SHOP, ADMIN_ACCESS_TOKEN

base_url = F"https://{USERNAME}:{PASSWORD}@{SHOP}.myshopify.com/admin/api/2022-10/"
headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': ADMIN_ACCESS_TOKEN}

def get_products():
    url = F"{base_url}products.json"
    res = requests.get(url, headers=headers)
    return res.text

def create_product():
    url = F"{base_url}products.json"
    body = {"product": {"title": "test create"}}
    res = requests.post(url, data={"title": "test create"}, headers=headers)
    return res.text
    
 
def delete_product(product_id):
    url = F"{base_url}/products/{product_id}.json"
    res = requests.delete(url, headers=headers)
    return res.status_code

# print(delete_product(8078773420305))
print(create_product())