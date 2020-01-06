# ** coding = "utf-8"
import random

class RecitationOfEnglish():
    def ens(self):
        wordl = []
        while True:
            op = input("是否录入单词「y or n」\n")
            if op == "n":
                print("录入单词结束！\n")
                break
            else:
                word = input("请输入单词及释义，eg: hello:你好\n")
                dic = {'单词': word.split(':')[0], '释义': word.split(':')[1]}
                wordl.append(dic)
        return wordl

    def recitation(self):
        lexicon = self.ens()
        print("***开始检测今天单词***")
        for i in range(10):
            word = random.choice(lexicon)
            print("释义：%s" % word["释义"])
            answer = input("请输入对应的英文:")
            if answer == word["单词"]:
                print("right!")
            else:
                print("wrong!")

if __name__ == '__main__':
    a = RecitationOfEnglish()
    a.recitation()





