import datetime

import pymongo


# pip install --upgrade pymongo
# openssl version
# python3 -c "import requests; print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])"
# /usr/lib/python3/dist-packages/urllib3/connectionpool.py:1020: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.howsmyssl.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   warnings.warn(
# TLS 1.3su

# sudo apt-get install build-essential python3-dev

# pip install pymongo[srv]

# dnspython


def db_connection():
    client = pymongo.MongoClient("mongodb+srv://")

    db = client.test

    collection = db.test_collection
    print(db.list_collection_names)
    print(collection.count_documents({}))

    post = {
        "author": "Maddo",
        "title": "Python for Java Developer",
        "tags": ["Java", "Python", "MongoDB"],
        "data": datetime.datetime.utcnow()
    }

    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
    print(db.posts)
    print(db.list_collection_names())

    orders = db.orders
    post_id = orders.insert_one(post).inserted_id
    print(post_id)
    print(db.orders)
    print(db.list_collection_names())

    pass


def print_hi(name):
    db_connection()

    print('Connected to MongoDB...')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
