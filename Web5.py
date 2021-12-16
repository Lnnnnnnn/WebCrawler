import requests
import re
import bs4
import time

url = "https://wall.alphacoders.com/tag/hatsune-miku-wallpapers"

resp = requests.get(url)
resp.encoding = "utf-8"

# obj = re.compile("a href(?P<test>.*?)<picture>.*?</picture></a>", re.S)
obj = re.compile("/big.php\?i=\d+", re.S)

result = obj.findall(resp.text)

result1 = list(map(lambda x : "https://wall.alphacoders.com/"+x, result))

for i in result1:
    child_page_resp = requests.get(i)
    child_page_resp.encoding = "utf-8"
    child_page_text = child_page_resp.text

    chil_page = bs4.BeautifulSoup(child_page_text,"html.parser")
    # img = chil_page.find("div", attrs = {"class"="center img-container-desktop"})
    p = chil_page.find("div", attrs= {"class":"center img-container-desktop",})
    image = p.find("a")
    # print(image.get("href"))
    # print(img.get('href'))
    src = image.get("href")
    # 下载图片
    image_resp = requests.get(src)
    image_name = src.split("/")[-1]
    with open("D:\PythonWebCrawler\image/"+image_name, mode='wb') as f:
        f.write(image_resp.content)
    print("over!!")
    time.sleep(1)


# print(resp.text)