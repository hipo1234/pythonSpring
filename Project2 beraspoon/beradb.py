from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve
import openpyxl

web = webdriver.Chrome()
web.get('https://zrr.kr/vN3b')
bs = BeautifulSoup(web.page_source, 'html.parser')

title = bs.find_all(id='cmdtName_S000201237157') # 책 제목 가져오기
intro = bs.find_all(class_='prod_desc') # 책 인트로 가져오기
image = bs.find_all(class_='prod_img_load') # 책 이미지 저장하기
print(title[0].text)
print(intro[0].text)
print(image[0].get('data-src'))
urlretrieve(image[0].get('data-src'), "springboot.jpg")


# python mysql
# sql = "insert into " + title[0].text
# cursor.execute(sql)

