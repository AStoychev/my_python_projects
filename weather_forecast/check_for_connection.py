import requests
from data import url


def internet_on():
    try:
        site = url["sofia"]
        timeout = 3
        r = requests.get(site, timeout=timeout)
        return True
    except requests.ConnectionError as ex:
        return False
