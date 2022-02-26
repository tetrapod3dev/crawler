from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from crawler.exportExcel import export_product_excel

depth = [('991001', '강아지간식'),
         ('991002', '강아지주식'),
         ('991003', '고양이간식'),
         ('991004', '고양이 주식'),
         ('991006', '반려동물 용품'),
         ('991007', '배변·위생'),
         ('991007', '소용량·샘플')]

url = "https://www.kurly.com/shop/goods/goods_list.php?category={}"


def web_crawler_loop():
    result = []
    for tu in depth:
        result.extend(get_products(url.format(tu[0]), tu[1]))
        time.sleep(1)
    return result


def get_products(url, category):
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:/work/crawl/src/chromedriver', options=op)
    driver.implicitly_wait(3)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="goodsList"]/div[1]/div/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(3)

    ul = driver.find_element(By.ID, "goodsList")\
        .find_element(By.CLASS_NAME, 'list_goods')\
        .find_element(By.CLASS_NAME, 'list')

    products = []
    rank = 1
    for item in ul.find_elements(By.CLASS_NAME, 'item'):
        name = item.find_element(By.CLASS_NAME, 'name').text

        image = item.find_element(By.TAG_NAME, 'img').get_attribute("src")

        price = item.find_element(By.CLASS_NAME, 'price').text.replace(",", "").replace("원", "")
        products.append({"순위": rank,
                         "제품명": name.strip(),
                         "제품이미지": image,
                         "가격": price,
                         "출처": '마켓컬리',
                         "구분1": category})
        rank = rank + 1
    print('[마켓컬리 - {}] size = {}'.format(category, len(products)))
    return products


file_path = '../../../doc/kurly.xlsx'
export_product_excel(web_crawler_loop(), file_path)
