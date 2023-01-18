"""
날짜 : 2023-01-17
이름 : 박진휘
내용 : 파이썬 기상청날씨 실습
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

#데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                user='root', 
                password='1234', 
                db='java1db', 
                charset='UTF8')

#가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

#기상청 이동
browser.get("https://www.weather.go.kr/w/obs-climate/land/city-obs.do")

#전국 도시명 출력
trs = browser.find_elements(By.CSS_SELECTOR, "#weather_table > tbody > tr")

for i in trs:
    tds = i.find_elements(By.CSS_SELECTOR, "td")
    val = []
    for j in tds:
        if j.text == '':
            val.append(None)
        else:
            val.append(j.text)
    #SQL 실행
    cur = conn.cursor()
    sql = "insert into `weather` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now());"
    cur.execute(sql, val)
    conn.commit()
    print('Insert 완료')

#데이터베이스 종료
conn.close()

#가상 브라우저 종료
browser.close()
print('프로그램 종료...')