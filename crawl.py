from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import re
from Goods import Goods
chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def chromeDriver(port, path_to_chrome=chromePath):
    subprocess.Popen("{chromePath} --remote-debugging-port={p}".format(chromePath=path_to_chrome, p=port))
    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:{p}".format(p=port))
    driver = webdriver.Chrome(options=options)
    return driver


def pddItem(keyword, attach_port=9222):
    driver = chromeDriver(port=attach_port)
    url = "https://youhui.pinduoduo.com/search/landing?keyword=" + quote(keyword)
    print(url)
    driver.get(url)
    time.sleep(1)
    goods = driver.find_elements_by_class_name("goods-detail-card-wrapper")

    good_list = []
    for good in goods:
        link = good.get_attribute("href")
        title = re.search("\S+\\n", good.text).group().strip("\n")
        price = float(re.search("￥(.*?)\\n", good.text).group().strip("\n").strip("￥"))
        good_instance = Goods(keyword=keyword, platform="PDD", link=link, title=title, price=price)
        print([title, price, "PDD"])
        good_list.append({"platform": "拼多多",
                          "keyword": keyword,
                          "title": title,
                          "price": price,
                          "link": link})
    driver.close()
    return good_list


def jdItem(keyword, attach_port=9223):
    driver = chromeDriver(port=attach_port)
    url = "https://search.jd.com/Search?keyword=" + quote(keyword)
    print(url)
    driver.get(url)
    goods = driver.find_elements_by_class_name("gl-i-wrap")

    good_list = []
    for good in goods:
        title_elem = good.find_element_by_class_name("p-name")
        title = title_elem.text
        link = title_elem.find_element_by_xpath("./a[1]").get_attribute("href")
        try:
            price = float(good.find_element_by_class_name("p-price").text.strip("￥"))
        except ValueError:
            price = float(good.find_element_by_class_name("p-price").text.strip("￥").split("\n")[0])
        good_instance = Goods(keyword=keyword, platform="JD", link=link, title=title, price=price)
        print([title, price, "JD"])
        good_list.append({"platform": "京东",
                          "keyword": keyword,
                          "title": title,
                          "price": price,
                          "link": link})
    driver.close()
    return good_list


def amzItem(keyword, attach_port=9224):
    driver = chromeDriver(port=attach_port)
    url = "https://www.amazon.cn/s?k=" + quote(keyword)
    print(url)
    driver.get(url)
    goods = driver.find_elements_by_xpath("//*[@data-component-type='s-search-result']")

    good_list = []
    for good in goods:
        title_elem = good.find_element_by_tag_name("h2")
        title = title_elem.text
        link = title_elem.find_element_by_xpath("./a[1]").get_attribute("href")
        try:
            price = float(re.search("\\n¥(.*?)\\n", good.text).group().strip("\n").strip("¥"))
        except:
            continue
        good_instance = Goods(keyword=keyword, platform="AMZ", link=link, title=title, price=price)
        good_list.append({"platform": "亚马逊",
                          "keyword": keyword,
                          "title": title,
                          "price": price,
                          "link": link})
        print([title, price, "AMZ"])
    driver.close()
    return good_list


def pddComment(link_to_item_page):
    """
    login required
    """
    driver = chromeDriver(chromePath, 9222)

    pass


def jdComment(link_to_item_page):
    pass


def amzComment(link_to_item_page):
    pass


if __name__ == '__main__':
    pass
