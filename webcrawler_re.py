import requests
import re
#1.指定url
url1 = 'https://wiki.biligame.com/ys/%E6%AD%A6%E5%99%A8%E4%B8%80%E8%A7%88'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
#2.发起请求、get方法会返回一个响应对象
response = requests.get(url=url1,headers=headers)
#3.获取响应数据.text返回字符串形式的响应数据
html = response.text
pattern = re.compile(r'src="http.+?png"')
pic_links = pattern.findall(html)
i = 1
for pic_link in pic_links:
    url = pic_link[5:-1]
    print(f"正在下载第{i}张图片：{url}...")
    pic_name = f'./pic2/{i}.png'
    response = requests.get(url=url,headers=headers)
    pic = response.content
    with open(pic_name, 'wb') as fp:
        fp.write(pic)
    i +=1
print("数据爬取完成！！！")
