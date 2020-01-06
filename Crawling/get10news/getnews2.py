# ** coding = 'utf-8'
import requests
from bs4 import BeautifulSoup

class GetHotNews():

#    soup = None
    def __init__(self, html):
        self.html = html
    '''
    def request(self):
        res = requests.get(self.html)
        res.encoding = 'utf-8'
        self.soup = BeautifulSoup(res.text, 'html.parser')
    '''
    def request(self):
        res = requests.get(self.html)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup

    def topMilitaryNews(self):
        hd = self.request().select('#hd')
        print("hd:{0}".format(hd))
    
    def topMilitaryPosts(self):
        pass

if __name__ == '__main__':
    test = GetHotNews("http://mil.news.sina.com.cn/hotnews/Daily/")

    test.topMilitaryNews()