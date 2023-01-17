"""
날짜 : 2023-01-16
이름 : 박진휘
내용 : 파이썬 HTML 요청 실습
pip install requests
"""
import requests as req

url = "http://naver.com"

html = req.get(url).text
print(html)