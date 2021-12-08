import time


class Goods():
    def __init__(self, keyword="", platform="", link="", title="", price=0.0):
        self.keyword = keyword
        self.platform = platform
        self.fetchTime = time.ctime()
        self.link = link
        self.title = title
        self.price = price