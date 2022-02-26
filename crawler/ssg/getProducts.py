from crawler.exportExcel import export_product_excel
from selenium import webdriver
from bs4 import BeautifulSoup
import time

from crawler.stringgetter import get_page_string

# depth = [('6000184955', '강아지사료/간식', '강아지사료', '건식사료'),
#          ('6000184956', '강아지사료/간식', '강아지사료', '소프트사료'),
#          ('6000184957', '강아지사료/간식', '강아지사료', '습식사료'),
#          ('6000184960', '강아지사료/간식', '강아지사료', '본유/우유'),
#          ('6000184967', '강아지사료/간식', '강아지간식', '껌'),
#          ('6000184968', '강아지사료/간식', '강아지간식', '건조간식/육포'),
#          ('6000184969', '강아지사료/간식', '강아지간식', '져키/트릿'),
#          ('6000184970', '강아지사료/간식', '강아지간식', '캔/파우치'),
#          ('6000184972', '강아지사료/간식', '강아지간식', '비스켓/기타'),
#          ('6000184979', '강아지사료/간식', '강아지영양제', '관절'),
#          ('6000184981', '강아지사료/간식', '강아지영양제', '유산균/장'),
#          ('6000184987', '고양이사료/간식', '고양이사료', '건식사료'),
#          ('6000184988', '고양이사료/간식', '고양이사료', '소프트사료'),
#          ('6000184992', '고양이사료/간식', '고양이사료', '분유/우유'),
#          ('6000184999', '고양이사료/간식', '고양이간식', '캔')]

# depth = [('6000185000', '고양이사료/간식', '고양이간식', '츄르/파우치'),
#          ('6000185001', '고양이사료/간식', '고양이간식', '덴탈간식/스택'),
#          ('6000185002', '고양이사료/간식', '고양이간식', '져키/통살'),
#          ('6000185004', '고양이사료/간식', '고양이간식', '캣닢/캣그라스'),
#          ('6000185005', '고양이사료/간식', '고양이간식', '기타간식'),
#          ('6000185022', '반려동물용품', '모래/배변용품', '배변패드'),
#          ('6000185023', '반려동물용품', '모래/배변용품', '배변판/배변매트'),
#          ('6000185024', '반려동물용품', '모래/배변용품', '모래'),
#          ('6000185026', '반려동물용품', '모래/배변용품', '배변봉투/모래삽/기타'),
#          ('6000185032', '반려동물용품', '위생/미용용품', '살균/탈취제'),
#          ('6000185035', '반려동물용품', '위생/미용용품', '칫솔/치약/구강세정제'),
#          ('6000185037', '반려동물용품', '위생/미용용품', '샴푸/린스/비누'),
#          ('6000185039', '반려동물용품', '위생/미용용품', '빗/가위/발톱깎이')]

depth = [('6000185050', '반려동물용품', '외출용품/의류', '이동장/캐리어'),
         ('6000185054', '반려동물용품', '외출용품/의류', '목줄/하네스'),
         ('6000185056', '반려동물용품', '외출용품/의류', '의류'),
         ('6000185057', '반려동물용품', '외출용품/의류', '시즌/액세서리'),
         ('6000185066', '반려동물용품', '하우스/캣타워', '반려동물매트'),
         ('6000185067', '반려동물용품', '하우스/캣타워', '방석/하우스'),
         ('6000185094', '반려동물용품', '식기/급식기', '자동급식기/정수기'),
         ('6000185095', '반려동물용품', '식기/급식기', '식기/물병'),
         ('6000185076', '반려동물용품', '강아지장난감/훈련', '봉제/라텍스장난감'),
         ('6000185077', '반려동물용품', '강아지장난감/훈련', '로프/치실'),
         ('6000185078', '반려동물용품', '강아지장난감/훈련', '노즈워크/IQ장난감'),
         ('6000185079', '반려동물용품', '강아지장난감/훈련', '원반/기타장난감')]

url = "https://www.ssg.com/disp/category.ssg?dispCtgId={}&sort=sale"


def web_crawler_loop():
    result = []
    for tu in depth:
        page_string = get_page_string(url.format(tu[0]))
        result.extend(get_products(page_string, tu[-3:]))
        time.sleep(1)
    return result


def get_products(string, category):
    bs_obj = BeautifulSoup(string, "html.parser")
    div = bs_obj.find("div", {"id": "ty_thmb_view"})  # 아이템 리스트부분 추출
    lis = div.findAll("li", {"class": "cunit_t232"})  # 각 아이템 추출

    products = []
    rank = 1
    for item in lis:
        # name
        div_name = item.find("em", {"class": "tx_ko"})
        name = div_name.getText()

        # image
        dt_image = item.find("div", {"class": "thmb"})
        image = dt_image.find("img").get('src')

        # price
        price = item.find("em", {"class": "ssg_price"}).getText().replace(",", "")

        products.append({"순위": rank,
                         "제품명": name.strip(),
                         "제품이미지": "https:" + image,
                         "가격": price,
                         "출처": 'SSG',
                         "구분1": category[0],
                         "구분2": category[1],
                         "구분3": category[2]})
        rank = rank + 1
    print('[SSG - {} - {} - {}] size = {}'.format(category[0], category[1], category[2], len(products)))
    return products


# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome('C:/work/crawl/src/chromedriver', options=op)
# driver.implicitly_wait(3)
# driver.get('https://www.ssg.com/disp/category.ssg?dispCtgId=6000185022')

file_path = '../../../doc/ssg3.xlsx'
export_product_excel(web_crawler_loop(), file_path)
