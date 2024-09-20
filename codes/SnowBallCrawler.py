import requests
import json
import time

class GZMaoTai:
    def __init__(self):

        self.url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json'
        self.div_id = 'div#KKE_range_1726148182941'
        self.headers = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Origin':'https://xueqiu.com',
            'Priority':'u=1, i',
            'Referer':'https://xueqiu.com/S/SH600519',
            'Cookie':'cookiesu=521725703998609; device_id=9bbe6c3575ad6f51a3db86a9fc8e4e95; xq_a_token=927886df384cbb16c88673ae7f519c76650c54b9; xqat=927886df384cbb16c88673ae7f519c76650c54b9; xq_r_token=1d46f0ed628506486164e5055a4993f9b54b2f4c; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyOTIxMjc4NCwiY3RtIjoxNzI2NzAyODE4ODQ4LCJjaWQiOiJkOWQwbjRBWnVwIn0.Tdg33X5uwvVrzvWToa6On_TVJdKJMk5VnPL-HcBHSuQqF14cPpPEzlVpNDM6mBwJxuS5sSOhA9dY1LcUivy90MaPyVFY0KLfG3CeWIVqMT5L1JIPfoW6NdW-ZrsQ_d4h1h5s62mMI4rY3e1csuONZv2SYX1el9RQEfeeLfU4QhA_5czYmR5hOEPqg7_UC4l-3PUbs613zSsaHGeJDa2-zbxPclZrYILIiebeMtZDUDejLIlBXfv3Krh_24Va3uqwSDz0RshTz2ISDC9WlP7maHnhB4x8O7wBOMiY1ceF8cpV17TA0USk4dIHNPsiw9bvj-gOnsEGDgzDJNYLyzSeUg; u=521725703998609; is_overseas=0; Hm_lvt_1db88642e346389874251b5a1eded6e3=1725704000,1726194524,1726626752,1726702834; HMACCOUNT=4DE46E99F3D985C3; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1726702869; ssxmod_itna=eqjxyD0DgDcDnCKDXDRDCxOERhhziAD0himC3hqGXxKoDZDiqAPGhDCb89reE3mx4KQWPe0QCb7ip44YWobxPAYCASEX=DU4i8DCuBI4bDen=D5xGoDPxDeDAiKiTDY4Dd6vTX=DEDeKDmxiODlIH6OiNRc9ODYvsDDHQCx07DQ5CYDDzYno46DGiD7eDEnK1CcAGW4D1KryDqnKD9OoDs2G6YnKmyId4BryL2bf3vrYhDCKDjo7kDmmHW8xCSr8PFrhqbmpYbinDK=iWtGGrejZiQQGqs709hwGYqih4+MueBu=DirDbe0xxD==; ssxmod_itna2=eqjxyD0DgDcDnCKDXDRDCxOERhhziAD0himC3xA6nhFD/YKWDFx7Ixmg9xyhgCbWG=qidcA7TY=+tCmjvNw+zRAYpC5Mang=HgYSwhxXPL9pYb+ejawj2vgR2DxqRIP+Cfqe8L29P7SAw4+DANgj5G/hKCFZewQcBktWBH/paWYpBho25v+EP+P+WtenKveBGd/EosYhWF0/msargfuCvdtrTFthujuQaFaO0TM/nW6le=qDLi1Aup4awTwl5qLZh=lCGt4VC8P0PPtYerQWdHlx9Da2GnKFupLpPr+WlDH99gaxM/t7I6EY+ZAxBmCxIcWjSawf704FjXxYvQtDheS2wDhmI2wXj0Eam+pAnBt4B+nDLxm4DQF/exN/PxIwt0FnzoWIhQurMFutSrECD/70WQh40Ofe8RK2Nv2YB+qlwq80ElhT6xWcrdD08DiQeYD=',
            'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }


    def get_response(self,date):
        nowtime = int(time.time() * 1000.0)
        print("当前时间: ",nowtime)
        param_data = {
            'symbol':'SH600519',
            'begin':str(nowtime),
            'period':'day',
            'type':'before',
            'count':'-284',
            'indicator':'kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance'
        }
        print("开始爬取数据")
        response = requests.get(self.url,headers=self.headers,params=param_data,timeout=5)
        print(response.text)
        print("爬取成功，数据包如上")

        data_json = json.loads(response.text)  # Json反序列化
        items = data_json['data']['item']
        # for i in range(len(items)):
        # print(items[i])
        # json数据对应
        # [0] timestamp
        # [1] 成交量
        # [2] 开盘价
        # [3] 最高价
        # [4] 最低价
        # [5] 收盘价
        # [6] 涨跌额
        # [7] 涨跌幅
        # [8] 换手率
        # [9] 成交额(亿)
        # [10] null
        # [11] null
        # [12]
        return items



if __name__ == '__main__':
    mt = GZMaoTai()
    mt.get_response(1)