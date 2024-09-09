import requests
from requests.exceptions import ReadTimeout,ConnectTimeout,ConnectionError,Timeout
import bs4 as bs
import lxml

# base_url = 'http://httpbin.org'
base_url = 'https://picbed.supdriver.top/html/adc_v2/index.html'
# para_data = {'user':'xmu','password':'123456'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
try:
    response = requests.get(base_url,headers=headers,timeout=0.5)
    print(response.content)
    print(response.text)
except ReadTimeout or ConnectTimeout or ConnectionError or Timeout:
    print('TimeOut')

soup = bs.BeautifulSoup(response.text,'lxml')
print('\n================================\n')
print(soup.h1.string)



