from crawler.stringgetter import get_page_string
from bs4 import BeautifulSoup


def get_products(string):
    bs_obj = BeautifulSoup(string, "html.parser")
    div = bs_obj.find("div", {"id": "ty_thmb_view"})  # 아이템 리스트부분 추출
    lis = div.findAll("li", {"class": "cunit_t232"})  # 각 아이템 추출

    products = []

    for item in lis:
        # name
        div_name = item.find("em", {"class": "tx_ko"})
        name = div_name.getText()
        # print("name:", name.strip())

        # image
        dt_image = item.find("div", {"class": "thmb"})
        image = dt_image.find("img").get('src')
        # print("image:", image)

        # price
        price = item.find("em", {"class": "ssg_price"}).getText().replace(",", "")
        # print("price:", price)
        products.append({"name": name.strip(), "image": "https:" + image, "price": price})

    print(len(products))
    return products


url = "https://www.ssg.com/disp/category.ssg?dispCtgId={}&sort=sale"
category = [{'id': 6000184886, 'name': "강아지사료"}]

pageString = get_page_string(url.format(category[0]['id']))
print(get_products(pageString))
