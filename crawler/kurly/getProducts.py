from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def get_products(url, category):
    ser = Service("C:/work/crawl/src/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.implicitly_wait(3)
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="goodsList"]/div[1]/div/div/div/ul/li[3]/a').click()
    driver.implicitly_wait(3)

    ul = driver.find_element(By.ID, "goodsList")\
        .find_element(By.CLASS_NAME, 'list_goods')\
        .find_element(By.CLASS_NAME, 'list')

    products = []

    for item in ul.find_elements(By.CLASS_NAME, 'item'):
        name = item.find_element(By.CLASS_NAME, 'name').text

        image = item.find_element(By.TAG_NAME, 'img').get_attribute("src")

        price = item.find_element(By.CLASS_NAME, 'price').text.replace(",", "").replace("원", "")
        products.append({"name": name.strip(), "image": image, "price": price, "category": category})

    print(len(products))
    return products


url = "https://www.kurly.com/shop/goods/goods_list.php?category={}"
category = [{'id': 991001, 'name': "강아지간식"},
            {'id': 991002, 'name': "강아지주식"},
            {'id': 991003, 'name': "고양이간식"},
            {'id': 991004, 'name': "고양이 주식"},
            {'id': 991006, 'name': "반려동물 용품"},
            {'id': 991007, 'name': "배변·위생"},
            {'id': 991007, 'name': "소용량·샘플"}]
print(get_products(url.format(category[0]['id']), category[0]['name']))

