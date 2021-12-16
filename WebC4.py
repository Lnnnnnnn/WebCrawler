# 定位2021位置
# 请求进入子页面的连接
# 进入连接，并且

import requests
import re

url = "https://www.dytt89.com/"

resp = requests.get(url,verify=False)
resp.encoding = "gb2312"

obj = re.compile(r"",re.S)



print(resp.text)

