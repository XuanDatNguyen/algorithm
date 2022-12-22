import requests

# Shop name
SHOP = "james-5030"
# Admin API access token
ADMIN_ACCESS_TOKEN = "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"

base_url = F"https://{SHOP}.myshopify.com/admin/api/2022-10/"
headers = {'Content-Type': 'application/json',
           'X-Shopify-Access-Token': ADMIN_ACCESS_TOKEN}


# Tạo mới smart collection
def create_smart_collection(body):
    url = F"{base_url}smart_collections.json"
    res = requests.post(url, headers=headers, json=body)
    return res.text


smart_body = {
    "smart_collection": {
        "title": "SSS Collections",
        "body_html": "Bộ sưu tập đến từ  brand SSSTUTTER",
        "rules": [
            {
                "column": "vendor",
                "relation": "equals",
                "condition": "SSSTUTTER"
            }
        ]
    }
}
# print(create_smart_collection(smart_body))


# Tạo mới custom collection
def create_custom_collection(body):
    url = F"{base_url}/custom_collections.json"
    res = requests.post(url, headers=headers, json=body)
    return res.text


custom_body = {
    "custom_collection": {
        "title": "Summer collections",
        "body_html": "Bộ sưu tập mùa hè năm nay với những item vô cùng hot chắc chắn sẽ khiến bạn hài lòng"
    }
}

# print(create_custom_collection(custom_body))


# Tạo mới sản phẩm
def create_product(data):
    url = F"{base_url}products.json"
    res = requests.post(url, json=data, headers=headers)
    return res.text


# Sản phẩm không có option
product = {
    "product": {
        "title": "CITY SWEATSHIRT",
        "vendor": "SSSTUTTER",
        "product_type": "Sweter",
        "status": "active",
    }
}

# Sản phẩm có option
product_o = {
    "product": {
        "title": "SMART PANTS",
        "body_html": "<p>Quần âu may kèm chun ẩn, co giãn</p>\n<p>Dáng suông thẳng, ống quần crop nhẹ</p>\n",
        "vendor": "SSSTUTTER",
        "product_type": "Jeans",
        "variants": [
            {
                "option1": "Be",
                "option2": "0",
                "inventory_management": "shopify",
            },
            {
                "option1": "Be",
                "option2": "1",
                "inventory_management": "shopify",
            },
            {
                "option1": "Đen",
                "option2": "0",
                "inventory_management": "shopify",
            },
            {
                "option1": "Đen",
                "option2": "1",
                "inventory_management": "shopify",
            }
        ],
        "options": [
            {
                "name": "Color",
                "values": ["Be", "Đen"]
            },
            {
                "name": "Size",
                "values": [0, 1]
            }
        ]
    }
}

# print(create_product(product_o))


# Cập nhật sản phẩm
def update_product(product_id, body):
    url = F"{base_url}products/{product_id}.json"
    res = requests.put(url, headers=headers, json=body)
    return res.text


# Update hình ảnh, giá, qty sản phẩm không có option
product_update = {
    "product": {
        "variants": [
            {
                "price": 356150,
                "compare_at_price": 419000,
                "inventory_quantity": 10,
            }
        ],
        "images": [
            {
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/112022/1667904313230.jpeg"
            },
            {
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/112022/1667804906083.jpeg"
            },
            {
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/122022/1671002395327.jpeg"
            }
        ]
    }
}

# Update hình ảnh, giá sản phẩm có option
product_update_o = {
    "product": {
        "variants": [
            {
                "id": 44250099319057,
                "price": 356150,
                "compare_at_price": 419000,
            },
            {
                "id": 44250099351825,
                "price": 356150,
                "compare_at_price": 419000,
            },
            {
                "id": 44250099384593,
                "price": 356150,
                "compare_at_price": 419000,
            },
            {
                "id": 44250099417361,
                "price": 356150,
                "compare_at_price": 419000,
            }
        ],
        "images": [
            {
                "position": 1,
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/062022/1655042533957.jpeg"
            },
            {
                "position": 2,
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/062022/1655042573549.jpeg"
            },
        ]
    }
}

product_id = 8083354550545
# print(update_product(product_id, product_update_o))


# Điều chỉnh số lượng sản phẩm có option
def adjust_inventory_qty(location_id, inventory_item_id, available_adjustment):
    url = F"{base_url}/inventory_levels/adjust.json"
    body = {"location_id": location_id, "inventory_item_id": inventory_item_id,
            "available_adjustment": available_adjustment}
    res = requests.post(url, headers=headers, json=body)
    return res.text
# print(adjust_inventory_qty(74947690769, 46298484277521, 5))


# Xóa sản phẩm
def delete_product(product_id):
    url = F"{base_url}/products/{product_id}.json"
    res = requests.delete(url, headers=headers)
    return res.status_code


# Tạo mới khách hàng
def create_customer(body):
    url = F"{base_url}customers.json"
    res = requests.post(url, json=body, headers=headers)
    return res.text


# Xóa khách hàng
def delete_customer(customer_id):
    url = F"{base_url}customers/{customer_id}.json"
    res = requests.delete(url, headers=headers)
    return res.status_code


customer = {
    "customer": {
        "first_name": "Nguyen Xuan",
        "last_name": "Dat",
        "email": "xuandatnguyen27@gmail.com",
        "phone": "0372545906",
        "verified_email": True,
        "addresses": [
            {
                "address1": "103a8, Khương Trung, Thanh Xuân, Hà Nội",
                "city": "Ha Noi",
                "country": "VN"
            }
        ]
    }
}
# print(create_customer(customer))
# print(delete_customer(6714770358545))


# Tạo mới order
def create_order(customer_id, variant_id, qty):
    url = F"{base_url}orders.json"
    body = {
        "order": {
            "line_items": [
                {
                    "variant_id": variant_id,
                    "quantity": qty
                }
            ],
            "customer": {
                "id": customer_id
            },
            "financial_status": "paid"
        }
    }
    res = requests.post(url, headers=headers, json=body)
    return res.text
# print(create_order(1, 2, 1))


# Xóa order
def delete_order(order_id):
    url = F"{base_url}orders/{order_id}.json"
    res = requests.delete(url, headers=headers)
    return res.status_code


print(delete_order(5222835454225))
