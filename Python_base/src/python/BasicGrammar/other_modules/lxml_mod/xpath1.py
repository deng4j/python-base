"""
一、xpath解析原理
1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。

表达式说明：
    /:表示的是从根节点开始定位。表示的是一个层级。
    //:表示的是多个层级。可以表示从任意位置开始定位。
    .:选取当前节点。
    ..:选取当前节点的父节点。
    @:选取属性。如@src

    属性定位：​​//div[@class='song']
    索引定位：​​//div[@class="song"]/p[3]​​ 索引是从1开始的。

    取文本：
​​      /text()​​获取的是标签中直系的文本内容
​​      //text()​​标签中非直系的文本内容（所有的文本内容）

    选取未知节点:
        *:匹配任何元素节点。
        @*:匹配任何属性节点。
        node():匹配任何类型的节点。
        ｜：或，如选取文档中的所有 title 和 price元素 //title | //price
"""

from lxml import etree


def getListResult(rs):
    print("\033[1;31m  ----------------------------------------------  \033[0m")

    for r in rs:
        print(etree.tostring(r, encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))

    print("\033[1;31m  ----------------------------------------------  \033[0m")


if __name__ == "__main__":
    # 实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('./file/source/index.html', etree.HTMLParser())

    rs = tree.xpath('/html/body/div')  # 获取html下面的body下面的div
    getListResult(rs)

    rs = tree.xpath('/html//div')  # 获取html下面的多个层级的div
    getListResult(rs)

    rs = tree.xpath('//div')  # 获取多个层级的div
    getListResult(rs)

    rs = tree.xpath('//div[@class="wrapper"]')  # 获取多个层级的div并且标签里面的class为wrapper
    getListResult(rs)

    # 获取多个层级的div并且标签里面的class为wrapper下面的多个层级的第五个li标签下的a标签里面的内容
    rs = tree.xpath('//div[@class="wrapper"]//li[5]/a/text()')[0]
    print(rs)

    rs = tree.xpath('//li[7]//text()')  # 多个层级的第七个li下的所有内容
    print(rs)

    rs = tree.xpath('//div[@class="wrapper"]//text()')  # 多个层级的div标签下的class为wrapper下的所有内容
    print(rs)

    rs = tree.xpath('//div[@class="wrapper"]//img/@src')  # 多个层级的div标签下的class为wrapper下的img属性的内容
    print(rs)
