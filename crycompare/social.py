import requests

__socialurl = 'https://www.cryptocompare.com/api/data/socialstats/?'
__miningurl = 'https://www.cryptocompare.com/api/data/miningequipment/'


def socialStats(id):
    return __get_data(__socialurl, id)


def miningEquipment():
    return __get_url(__miningurl)


def __get_data(urlbase, id):
    url = urlbase + 'id=' + str(id)
    raw_data = requests.get(url)
    raw_data.encoding = 'utf-8'
    if raw_data.status_code != 200:
        raw_data.raise_for_status()
        return False
    try:
        return raw_data.json()['Data']
    except NameError:
        raise ValueError('Cannot parse to json.')


def __get_url(url):
    raw_data = requests.get(url)
    raw_data.encoding = 'utf-8'
    if raw_data.status_code != 200:
        raw_data.raise_for_status()
        return False
    try:
        return raw_data.json()['Data']
    except NameError:
        raise ValueError('Cannot parse to json.')
