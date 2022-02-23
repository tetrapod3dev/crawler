import requests


def get_page_string(url, headers=None, params=None):
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/98.0.4758.102 Safari/537.36'}
    data = requests.get(url, headers=headers, params=params)
    return data.content
