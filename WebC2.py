import json

import requests


url = "https://fanyi.baidu.com/sug"

dat = {
    "kw" : "dog"
}

resp = requests.post(url, data=dat)

with open("D:\PythonWebCrawler\webdownload\web2.text","w",encoding='utf-8') as filename:
    json.dump(resp.text,filename)



print(resp.json())
print("over")

