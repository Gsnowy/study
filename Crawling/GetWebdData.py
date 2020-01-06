# ** coding = 'utf-8'
import requests
from bs4 import BeautifulSoup as BS4

url = "https://news.sina.com.cn/gov/xlxw/2019-12-30/doc-iihnzahk0894800.shtml"
res = requests.get(url)
res.encoding = "utf-8"
#print(type(res),"\n")  # <class 'requests.models.Response'>
#print(res.text)    # 获取respond结果

soup = BS4(res.text, 'html.parser')
#print(type(soup))   # <class 'bs4.BeautifulSoup'>
#print(soup.text)   # 去标签
a_list = soup.select('a')  # 获取a标签，值为list
'''
for a in a_list:
    try:
        a_href = a['href']  # 获取 a 标签中的 href 属性
        a_text = a.text # 获取 a 标签中的内容
        print(a_href,a_text)
    except KeyError as err:
        print('该a标签不存在href属性')
'''
'''取得含有特定css属性的元素，eg:使用select找到所有id为title的元素：soup.select(‘#title’),使用select找到所有class为link的元素：soup.select(‘.link’)'''
'''获取文章标题title,来源from,作者author,发布时间publish_time,文章内容content'''
title_list = soup.select('.main-title')
title = title_list[0].text
#print(title)

'''[<a class="source" data-sudaclick="content_media_p" href="http://m.news.cctv.com/2019/12/30/ARTII8y7xjhkuzUJqppYiiNQ191230.shtml" 
rel="nofollow" target="_blank">央视</a>]

source = soup.select('.source')[0].text
source_html = soup.select('.source')[0]['href']


publish_time_list = soup.select('.date')
publish_time = publish_time_list[0].text
print(publish_time)

author_list = soup.select('.show_author')
author = author_list[0].text
author = author.split('：')[1]
print(author)
'''
'''等价操作 con = '\n'.join([p.text.strip() for p in soup.select('#article p')[:-1]])'''
content_list = soup.select('#article p')[:-1]   # 获取class = article 下的所有p标签的内容
content = []
for p in content_list:
    content.append(p.text.strip())
con = '\n'.join(content)    # 将段落以换行符分割连接在一起，将列表转换为字符串

con1 = '\n'.join([p.text.strip() for p in soup.select('#article p')[:-1]])
print(con1)


