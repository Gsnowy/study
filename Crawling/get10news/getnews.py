# ** coding = 'utf-8'
import requests
from bs4 import BeautifulSoup

class GetHotNews():

    def __init__(self, html):
        self.html = html

    def gethtml(self):
        res = requests.get(self.html)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def topMilitaryNews(self):
        soup = self.gethtml()

        for hd in soup.select('.linkNews'):
            print(hd)


    def topMilitaryPosts(self):
        pass

if __name__ == '__main__':
    test = GetHotNews("http://mil.news.sina.com.cn/hotnews/Daily/")
    test.topMilitaryNews()