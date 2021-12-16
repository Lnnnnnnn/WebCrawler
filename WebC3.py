import requests
import json

url = "https://movie.douban.com/j/chart/top_list"


para = {
    "type":"11",
    "interval_id":"100:90",
    "action":"",
    "start":"100",
    "limit":"1000"
}

header = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}
# json的格式需要修改

resp = requests.get(url=url,params=para,headers=header)


with open("D:\PythonWebCrawler\webdownload\web3.json","w",encoding='utf-8') as filename:
    json.dump(resp.text,filename)


print(resp.json())
resp.close() 