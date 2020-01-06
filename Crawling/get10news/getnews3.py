# ** coding = 'utf-8'
import requests
from bs4 import BeautifulSoup

class GetHotNews():

        res = requests.get("http://mil.news.sina.com.cn/hotnews/Daily/")
#        print("res:{0}".format(res))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
#        print(type(soup))
#        print("soup:{0}".format(soup))

    def topMilitaryNews(self):

        hd = self.soup.select('#hd')
        print("hd:{0}".format(hd))
    def topMilitaryPosts(self):
        pass

if __name__ == '__main__':
    test = GetHotNews("http://mil.news.sina.com.cn/hotnews/Daily/")
    test.topMilitaryNews()