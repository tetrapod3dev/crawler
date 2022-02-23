from crawler.stringgetter import get_page_string
from bs4 import BeautifulSoup


def get_products(string):
    bs_obj = BeautifulSoup(string, "html.parser")
    ul = bs_obj.find("ul", {"id": "productList"})  # 아이템 리스트부분 추출
    lis = ul.findAll("li", {"class": "baby-product renew-badge"})  # 각 아이템 추출

    products = []

    for item in lis:
        # name
        div_name = item.find("div", {"class": "name"})
        name = div_name.getText()
        # print("name:", name.strip())

        # image
        dt_image = item.find("dt", {"class": "image"})
        image = dt_image.find("img").get('src')
        # print("image:", image)

        # price
        price = item.find("strong", {"class": "price-value"}).getText().replace(",", "")
        # print("price:", price)
        products.append({"name": name.strip(), "image": "https:" + image, "price": price})

    print(len(products))
    return products


url = "https://www.coupang.com/np/categories/445726?listSize=60&page=1&channel=user&fromComponent=N&sorter=saleCountDesc&component=445626"


pageString = get_page_string(url, (('listSize', '60'), ('page', '1')))
print(get_products(pageString))
