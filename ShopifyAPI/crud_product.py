import requests
from settings import USERNAME, PASSWORD, SHOP, ADMIN_ACCESS_TOKEN

base_url = F"https://{SHOP}.myshopify.com/admin/api/2022-10/"
headers = {'Content-Type': 'application/json',
           'X-Shopify-Access-Token': ADMIN_ACCESS_TOKEN}


# def delete_product(product_id):
#     url = F"{base_url}/products/{product_id}.json"
#     res = requests.delete(url, headers=headers)
#     return res.status_code


# Đọc hiểu API về product, collection, customer, order.
# Create:
# Collection: 1 Smart collection, 1 Custom collection.
# Product: 1 Product không option, 1 Product có 2 options (Size, Color,...).
# Customer: 1 customer (có thể lấy thông tin chính bản thân).
# Order: tạo 1 order cho customer khi mua product đã tạo bên trên.
# Update: cập nhật giá, cập nhật ảnh, cập nhật số lương (qty) cho 2 product vừa tạo.
# Delete: Xoá toàn bộ dữ liệu vừa tạo.


# -----Smart collection-----
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


# -----Custom collection-----
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

# -----Product-----


def create_product(data):
    url = F"{base_url}products.json"
    res = requests.post(url, json=data, headers=headers)
    return res.text


# Product without option
product = {
    "product": {
        "title": "CITY SWEATSHIRT",
        "vendor": "SSSTUTTER",
        "product_type": "Sweter",
        "status": "active",
    }
}


# Product with option size & color
product_o = {
    "product": {
        "title": "SMART PANTS",
        "body_html": "<p>Quần âu may kèm chun ẩn, co giãn</p>\n<p>Dáng suông thẳng, ống quần crop nhẹ</p>\n",
        "vendor": "SSSTUTTER",
        "product_type": "Jeans",
        "variants": [
            {
                "option1": "Be",
                "option2": "0"
            },
            {
                "option1": "Be",
                "option2": "1"
            },
            {
                "option1": "Đen",
                "option2": "0"
            },
            {
                "option1": "Đen",
                "option2": "1"
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
print(create_product(product_o))

# 8081258709265, 8081380180241

update_product = {
    "product": {
        "images": [
            {
                "position": 1,
                "src": "https://cdn.ssstutter.com/products/po0EUQXd52Ks47dT/112022/1667904313230.jpeg"
            }
        ]
    }
}


def update_product(product_id, body):
    url = F"{base_url}/products/{product_id}.json"
    res = requests.put(url, headers=headers, json=body)
    return res.text
# -----Customer-----


def create_customer(body):
    url = F"{base_url}customers.json"
    res = requests.post(url, json=body, headers=headers)
    return res.text


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
# -----Order-----#
