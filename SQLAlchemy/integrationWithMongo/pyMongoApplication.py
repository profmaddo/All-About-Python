import pymongo
# pip install --upgrade pymongo
# openssl version
# python3 -c "import requests; print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])"
# /usr/lib/python3/dist-packages/urllib3/connectionpool.py:1020: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.howsmyssl.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
#   warnings.warn(
# TLS 1.3su

# sudo apt-get install build-essential python3-dev



def print_hi(name):
    client = pymongo.MongoClient("mongodb+srv://user:secreto@clusterpymongo.topsecret.mongodb.net/")

    VALOR = 0


    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
