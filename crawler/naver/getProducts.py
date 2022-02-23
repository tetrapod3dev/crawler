import json  # 추가
import requests


def get_products(category):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    }

    params = (
        ('sort', 'rel'),
        ('pagingIndex', '1'),
        ('pagingSize', '40'),
        ('viewType', 'list'),
        ('productSet', 'total'),
        ('catId', category['id']),
        ('spec', ''),
        ('deliveryFee', ''),
        ('deliveryTypeValue', ''),
        ('iq', ''),
        ('eq', ''),
        ('xq', ''),
    )

    response = requests.get('https://search.shopping.naver.com/api/search/category/{}'.format(category['url']),
                            headers=headers, params=params)

    # 여기서부터 추가코드-----------------------------
    itemlist = json.loads(response.text)

    products = []

    for i in itemlist['shoppingResult']['products']:
        title = i['productTitle']
        price = i['price']
        image = i['imageUrl']
        products.append({"name": title, "image": image, "price": price, "category": category['name']})

    return products


category = [{'url': 100000751, 'id': 50006631, 'name': "건식"},
            {'url': 100000752, 'id': 50008289, 'name': "동결건조"},
            {'url': 100000753, 'id': 50006635, 'name': "분유/우유"},
            {'url': 100000754, 'id': 50006632, 'name': "소프트"},
            {'url': 100000755, 'id': 50006634, 'name': "수제"},
            {'url': 100000756, 'id': 50006633, 'name': "습식"},
            {'url': 100000757, 'id': 50006630, 'name': "화식"},
            {'url': 100000730, 'id': 50006637, 'name': "개껌"},
            {'url': 100000734, 'id': 50006639, 'name': "수제간식"},
            {'url': 100000735, 'id': 50006638, 'name': "육포/건조"},
            {'url': 100000731, 'id': 50006641, 'name': "동결건조"},
            {'url': 100000732, 'id': 50006640, 'name': "비스킷/스낵"},
            {'url': 100000733, 'id': 50008408, 'name': "빵/케이크"},
            {'url': 100000736, 'id': 50006645, 'name': "음료"},
            {'url': 100000737, 'id': 50006642, 'name': "캔/파우치"},
            {'url': 100000738, 'id': 50006644, 'name': "통살/소시지"},
            {'url': 100000739, 'id': 50006643, 'name': "트릿/스틱"}]

print(get_products(category[-1]))
