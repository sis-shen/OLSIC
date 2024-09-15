import requests
import json
from bs4 import  *
import time

class GZMaoTai:
    def __init__(self):

        self.url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json'
        self.div_id = 'div#KKE_range_1726148182941'
        self.headers = {
            'Accept':'application/json, text/plain, */*',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie':'xq_a_token=49c5e355d2fc1b871fde601c659cf9ae1457a889; xqat=49c5e355d2fc1b871fde601c659cf9ae1457a889; xq_r_token=250d5a132310b89c6cf1193e084989736506a297; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcyNzkxNjc3OCwiY3RtIjoxNzI1NzAzOTQwOTczLCJjaWQiOiJkOWQwbjRBWnVwIn0.PBc_s7CP5jStz7xIu4H39jWKdiz3n4033BTdWwCxHcfQzcdleMmmVPl_lX3HmLKKvMFkPJJzAUCl0dGks6ThWgrfpG9iqPDGkP0GHhQflgsX6ynBr2ZFmtDA-59W2mS4qafql9UfmmPWGygqr-rK_am7k_X1gF6MxWouYBvtxL2dAMhSkgloQbR4IzQnN1FGCdyeEFb63EUddUKS80ZAlSGHG386kaIti9ULCQyfdoC890lLo_PVH0aU5-UgNd436IsDLJqpobZ2HJWvy-57OKePHMzjGL6T5YS34qDzA5fApRZNwYOUFgNg9LOLQvd8f_sQt_hTQrFebQ7fJzPooQ; cookiesu=521725703998609; u=521725703998609; device_id=9bbe6c3575ad6f51a3db86a9fc8e4e95; Hm_lvt_1db88642e346389874251b5a1eded6e3=1725704000; HMACCOUNT=4DE46E99F3D985C3; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1725704059; ssxmod_itna=Qq0x0DRDnD90KY5P0de0PwP=x2DUxxAKNqPwiYUREwtD/B4vDnqD=GFDK40EEkpFYbeSWYHe5nhm5HiznCGxH5WBbfhtTDCPGnDB9G=C7QxiiMDCeDIDWeDiDGbOD=xGYDjBIz1yDm4i7DiKDpx0kzgI55QvkAxGCVxDCc0PDwx0C2ODDBOGvKeqD4xGrDm+kc2pwqFoDn=i1C0hkD7ypDlaYy8Gkr+LUKmH103kEUGFhP40OD09GUxibzaEP26HEaWc4TGP4eQhrCQD5eYhxq0DPhjt53GDqzihBKiD5YD2B72xyOODDighmiKtYD==; ssxmod_itna2=Qq0x0DRDnD90KY5P0de0PwP=x2DUxxAKNqPwiYUREqG98OiDBkirx7PttmM7OMkP4bB5hk3GemhjiQRhYg5qRDn4NfCUhGw+fHuRAdaChS=iIhCqtRgvFzq8kexlOKgjz0Qtpg5llFNPnWCBWzuiy=WOW=RGGTWPHi6ZA+30BOC7n7zQAQPfAiqmgai=EkFpIznAYALUKF1tfQiSHCtf7OL+aLZnKXfKbaLp9pahT2VFIfiQjF82G5a6TtK36aL2rbM+0Cg1IalAgEFhq45ScCRtq9gj=Ml0qxeO8fV2W8rR7k3CcAx65CGPq=w8E3ecfjjfjiP11K7hqT03LD0oF5W2qwZpkQNnee67QfBe1WrjB6b83Zitoo32nGwGtrIrO=pKb0MENyhRclUfnoP/dKIprBrjC2KfAe1dfmeMcYmtiN=KPgmttc+aTwC0Eco5RckALs=bD94DQKs+9vbTn+bTRrTmKoOMk14eeI3Sh50rhR4eK0bmLzLFFtG8c4xGTYRIxIPoMF+HqxlDDFqD+ODxD===',
            'Origin':'https://xueqiu.com',
            'Priority':'u=1, i',
            'Referer':'https://xueqiu.com/S/SH600519',
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