from lib2to3.pgen2 import driver
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup()

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
from limitedframes.models import Photoism
#리눅스 여기추가
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
#-----------------------



# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# //*[@id="mount_0_0_tN"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]
# /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]
def parse_photoism():
  id = input('instagram 아이디 및 계정 입력 : ')
  pw = input('instagram 패스워드 입력 : ')
  result = []

  baseUrl = 'https://www.instagram.com/photoism.kr/'
  #리눅스 여기추가
  path = '/home/ubuntu/FilmArchive/chromedriver'
  driver = webdriver.Chrome(path,chrome_options=chrome_options)
  #----------------------------------

  # driver = webdriver.Chrome()
  driver.get('https://www.instagram.com/accounts/login/')
  # driver.get(baseUrl)
  time.sleep(2)
  # loginForm > div > div:nth-child(1) > div > label > input
  # id_input = driver.find_element_by_css_selector(
  #     '#loginForm > div > div:nth-child(1) > div > label > input')
  idpath = '#loginForm > div > div:nth-child(1) > div > label > input'
  pwpath = '#loginForm > div > div:nth-child(2) > div > label > input'
  id_input = driver.find_element(By.CSS_SELECTOR,idpath);
  pw_input = driver.find_element(By.CSS_SELECTOR,pwpath);
  # pw_input = driver.find_element_by_css_selector(
  #     '#loginForm > div > div:nth-child(2) > div > label > input')

  time.sleep(4)
  id_input.send_keys(id)
  pw_input.send_keys(pw)
  pw_input.submit()

  time.sleep(3)

  save_late_button1 = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
  save_late_button1.click()

  driver.implicitly_wait(3)

  #리눅스 2번째 버튼제거 도윤이 임시계정사용 크롤링
  # save_late_button2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
  # save_late_button2.click()

  driver.get(baseUrl)
  time.sleep(5)

  for i in range(0,2):
    
    

    html = driver.page_source
    soup = bs(html, "html.parser")
    photoismitems = soup.select("._aabd._aa8k._aanf")
    time.sleep(5)
    # print(photoismitems)

    for index,photoismitem in enumerate(photoismitems):
      photoismphoto = photoismitem.select_one("img").get("src")
      photoismid = photoismitem.select_one("a").get("href")
      with urlopen(photoismphoto) as f:
              with open('./static/imgphotoism/' + 'photoism' + photoismid[3:-1] + '.jpg', 'wb') as h:  # wb는 쓰기모드 + 바이너리모드. 이미지이기때문에 b모드를 써줘야한다.
                  print('h',h)
                  image = f.read()  # f를 읽어와서 img라는 변수 안에 저장 
                  # print('image',image) 이파일 픽셀값임
                  h.write(image)  # 가져온 이미지를 해당 경로에 지정된 이름으로 저장
                  photoismphotourl = 'imgphotoism/' +'photoism' + photoismid[3:-1] + '.jpg'
                
                
      photoismurl = "https://www.instagram.com/photoism.kr" + photoismitem.select_one("a").get("href")
      photoismphotoinfo = photoismitem.select_one("img").get("alt")
      
      item_obj = {
          'photoismphoto': photoismphoto,
          'photoismphotourl': photoismphotourl,
          'photoismurl': photoismurl,
          'photoismphotoinfo': photoismphotoinfo,
          'photoismid': photoismid,
      }
      print(photoismphotoinfo)
      result.append(item_obj)
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(5)
  driver.close()
  return result

def add_new_items(crawled_items):
    last_inserted_items = Photoism.objects.last()
    if last_inserted_items is None:
        last_inserted_specific_id = ""
    else:
        last_inserted_specific_id = getattr(last_inserted_items, 'photoismid')

    items_to_insert_into_db = []
    for item in crawled_items:
        if item['photoismid'] == last_inserted_specific_id:
            break
        items_to_insert_into_db.append(item)
    items_to_insert_into_db.reverse()

    for item in items_to_insert_into_db:
        print("new item added!! : " + item['photoismphotoinfo'])

        Photoism(photoismphoto=item['photoismphoto'],
                photoismphotourl=item['photoismphotourl'],
                photoismurl=item['photoismurl'],
                photoismphotoinfo=item['photoismphotoinfo'],
                photoismid = item['photoismid']).save()

    return items_to_insert_into_db

if __name__ == '__main__':
    add_new_items(parse_photoism())