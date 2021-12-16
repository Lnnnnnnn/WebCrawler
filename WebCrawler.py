import requests


url = "https://www.google.com/search?q=python"

dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win32; x3211) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}

resp = requests.get(url,headers=dic)


with open("D:\PythonWebCrawler\webdownload\web1.html","w",encoding='utf-8') as filename:
    filename.write(resp.text)


print(resp.request.headers)

