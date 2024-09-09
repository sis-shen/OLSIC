import urllib3
import requests
from requests.exceptions import ReadTimeout,ConnectTimeout,ConnectionError,Timeout
import bs4 as bs
import lxml
from functions import  *
# 获取名句页面
base_url = 'https://www.gushiwen.cn/mingjus/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
try:
    response = requests.get(base_url,headers=headers,timeout=0.5)
    soup = bs.BeautifulSoup(response.text,'lxml')
    with open('mingju.txt','w',encoding='utf-8') as file:
        file.write(soup.prettify())

    names = soup.select('div.main3 > div.left > div.sons > div.cont > a:nth-of-type(2)')
    print("============开始爬取==============")
    for i in range(len(names)%5):
        name_ = str(names[i].get_text())
        name_ = name_.replace('/','或')
        print(name_)
        filename ='./output/' + str(i+1) + name_ + '.txt'

        href = names[i].get('href')
        conts = getContent(href,headers)
        with open(filename,'w',encoding='utf-8') as file:
            for j in range(len(conts)):
                text = conts[j].get_text()
                if text.count(' ') >= len(text)-2 :
                    continue
                file.write(text)

except ReadTimeout or ConnectTimeout or ConnectionError or Timeout:
    print('TimeOut')

print("==========爬取完成================")
print("总计" , len(names))



