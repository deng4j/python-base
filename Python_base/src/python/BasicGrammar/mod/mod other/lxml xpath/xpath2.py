import requests
from lxml import etree

if __name__ == '__main__':
    url = 'http://www.syiban.com/search/index/init.html?modelid=1&q=肃肃宵征'
    response = requests.get(url=url)
    page_text = response.text

    tree = etree.HTML(page_text)
    str = etree.tostring(tree).decode()
    print(str)

    question = tree.xpath('//span[@class="title_color"]')
    answer = tree.xpath('//div[@class="yzm-news-right"]/p/span')
    for index, value in enumerate(question):
        print(question[index].xpath('string()'))
        print(answer[index].xpath('string()'))
    # 持久化存储
    with open('file/download/强国.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
