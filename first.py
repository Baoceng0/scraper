from urllib.request import urlopen

url = "http://www.qq.com"
rsp = urlopen(url)
print(rsp.read().decode('gb2312'))