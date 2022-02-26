import json  # 추가
import requests
import time

from crawler.exportExcel import export_product_excel

depth = [('100000751', '50006631', '강아지용품', '사료', '건식'),
         ('100000752', '50008289', '강아지용품', '사료', '동결건조'),
         ('100000753', '50006635', '강아지용품', '사료', '분유/우유'),
         ('100000756', '50006633', '강아지용품', '사료', '습식'),
         ('100000730', '50006637', '강아지용품', '간식', '개껌'),
         ('100000735', '50006638', '강아지용품', '간식', '육포/건조'),
         ('100000731', '50006641', '강아지용품', '간식', '동결건조'),
         ('100000732', '50006640', '강아지용품', '간식', '비스킷/스낵'),
         ('100000736', '50006645', '강아지용품', '간식', '음료'),
         ('100000737', '50006642', '강아지용품', '간식', '캔/파우치'),
         ('100000738', '50006644', '강아지용품', '간식', '통살/소시지'),
         ('100000739', '50006643', '강아지용품', '간식', '트릿/스틱'),
         ('100000749', '50006647', '강아지용품', '배변용품', '배변패드'),
         ('100000748', '50006648', '강아지용품', '배변용품', '배변판'),
         ('100000746', '50006653', '강아지용품', '배변용품', '배변봉투/집게'),
         ('100000750', '50006650', '강아지용품', '배변용품', '탈취제/소독제'),
         ('100000743', '50006655', '강아지용품', '건강/관리용품', '영앙제'),
         ('100000740', '50006656', '강아지용품', '건강/관리용품', '유산균'),
         ('100000766', '50006727', '강아지용품', '리빙용품', '매트'),
         ('100000770', '50006725', '강아지용품', '리빙용품', '쿠션/방석'),
         ('100000771', '50006726', '강아지용품', '리빙용품', '하우스'),
         ('100000783', '50006749', '강아지용품', '이동/산책용품', '가슴줄'),
         ('100000784', '50006751', '강아지용품', '이동/산책용품', '리드줄'),
         ('100000786', '50006748', '강아지용품', '이동/산책용품', '목줄'),
         ('100000787', '50006737', '강아지용품', '이동/산책용품', '물병'),
         ('100000777', '50006665', '강아지용품', '미용/목욕', '브러시/빗'),
         ('100000779', '50006663', '강아지용품', '미용/목욕', '샴푸/린스/비누'),
         ('100000774', '50008348', '강아지용품', '미용/목욕', '물티슈/크리너'),
         ('100000781', '50006670', '강아지용품', '미용/목욕', '타월/가운'),
         ('100000790', '50006737', '강아지용품', '식기/급수기', '급수기/물병'),
         ('100000791', '50006739', '강아지용품', '식기/급수기', '사료통/사료스풉'),
         ('100000792', '50006735', '강아지용품', '식기/급수기', '식기/식탁'),
         ('100000759', '50006674', '강아지용품', '장난감/훈련', '노즈워크'),
         ('100000761', '50006675', '강아지용품', '장난감/훈련', '장난감/토이'),
         ('100000758', '50006676', '강아지용품', '장난감/훈련', '공/원반'),
         ('100000813', '50006731', '강아지용품', '패션용품', '티셔츠/후드'),
         ('100000809', '50007153', '강아지용품', '패션용품', '원피스/드레스'),
         ('100000807', '50006730', '강아지용품', '패션용품', '올인원'),
         ('100000812', '50007158', '강아지용품', '패션용품', '코스튬'),
         ('100000818', '50007165', '강아지용품', '패션용품', '헤어핀/주얼리'),
         ('100000799', '50006733', '강아지용품', '패션용품', '기타액세서리'),
         ('100000852', '50008388', '고양이용품', '사료', '동결건조'),
         ('100000851', '50006679', '고양이용품', '사료', '건식'),
         ('100000855', '50006680', '고양이용품', '사료', '습식'),
         ('100000833', '50006685', '고양이용품', '간식', '캔/파우치'),
         ('100000827', '50006688', '고양이용품', '간식', '동결건조'),
         ('100000834', '50006692', '고양이용품', '간식', '캣닢/캣그라스'),
         ('100000836', '50006689', '고양이용품', '간식', '트릿/스틱'),
         ('100000831', '50006687', '고양이용품', '간식', '육포/건조'),
         ('100000828', '50006691', '고양이용품', '간식', '비스킷/스택'),
         ('100007138', '50006693', '고양이용품', '간식', '음료'),
         ('100000850', '50006696', '고양이용품', '배변용품', '흡수형모래'),
         ('100000845', '50006695', '고양이용품', '배변용품', '응고형모래'),
         ('100000842', '50006702', '고양이용품', '배변용품', '매트/발판'),
         ('100000847', '50006701', '고양이용품', '배변용품', '탈취제/소독제'),
         ('100000844', '50006703', '고양이용품', '배변용품', '분변통/모래삽'),
         ('100000843', '50006700', '고양이용품', '배변용품', '배변패드')]


def web_crawler_loop():
    result = []
    for tu in depth:
        result.extend(get_products(tu))
        time.sleep(1)
    return result


def get_products(category):
    headers = {
        'authority': 'search.shopping.naver.com',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36',
    }

    params = (
        ('sort', 'rel'),
        ('pagingIndex', '1'),
        ('pagingSize', '40'),
        ('viewType', 'list'),
        ('productSet', 'total'),
        ('catId', category[1]),
        ('spec', ''),
        ('deliveryFee', ''),
        ('deliveryTypeValue', ''),
        ('iq', ''),
        ('eq', ''),
        ('xq', ''),
    )

    response = requests.get('https://search.shopping.naver.com/api/search/category/{}'.format(category[0]),
                            headers=headers, params=params)

    item_list = json.loads(response.text)

    products = []
    rank = 1
    for i in item_list['shoppingResult']['products']:
        title = i['productTitle']
        price = i['price']
        image = i['imageUrl']
        products.append({"순위": rank,
                         "제품명": title.strip(),
                         "제품이미지": image,
                         "가격": price,
                         "출처": '네이버쇼핑',
                         "구분1": category[2],
                         "구분2": category[3],
                         "구분3": category[4]})
        rank = rank + 1
    print('[NAVER - {} - {} - {}] size = {}'.format(category[2], category[3], category[4], len(products)))
    return products


file_path = '../../../doc/naver.xlsx'
export_product_excel(web_crawler_loop(), file_path)
