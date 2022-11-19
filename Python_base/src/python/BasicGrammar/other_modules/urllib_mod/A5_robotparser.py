import urllib.robotparser

"""
class urllib.robotparser.RobotFileParser(url='')：用于解析 robots.txt 文件。robots.txt（统一小写）是一种
    存放于网站根目录下的 robots 协议，它通常用于告诉搜索引擎对网站的抓取规则。
    
        set_url(url) - 设置 robots.txt 文件的 URL。
        read() - 读取 robots.txt URL 并将其输入解析器。
        parse(lines) - 解析行参数。
        can_fetch(useragent, url) - 如果允许 useragent 按照被解析 robots.txt 文件中的规则来获取 url 则返回 True。
        mtime() -返回最近一次获取 robots.txt 文件的时间。 这适用于需要定期检查 robots.txt 文件更新情况的长时间运行的网页爬虫。
        modified() - 将最近一次获取 robots.txt 文件的时间设置为当前时间。
        crawl_delay(useragent) -为指定的 useragent 从 robots.txt 返回 Crawl-delay 形参。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
        request_rate(useragent) -以 named tuple RequestRate(requests, seconds) 的形式从 robots.txt 返回 Request-rate 形参的内容。 如果此形参不存在或不适用于指定的 useragent 或者此形参的 robots.txt 条目存在语法错误，则返回 None。
        site_maps() - 以 list() 的形式从 robots.txt 返回 Sitemap 形参的内容。 如果此形参不存在或者此形参的 robots.txt 条目存在语法错误，则返回 None。
        
robots.txt：
    禁止所有爬虫访问任何内容
        User-Agent:  *
        Disallow:  /
    允许所有爬虫访问任何内容
        User-Agent:  *
        Disallow: 
    只允许爬虫访问 public/ 目录    
        User-agent: *
        Disallow: /
        Allow: /public/
"""

rp = urllib.robotparser.RobotFileParser()

rp.set_url("http://www.musi-cal.com/robots.txt")

rp.read()

fetch = rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
print(fetch)

can_fetch = rp.can_fetch("*", "http://www.musi-cal.com/")
print(can_fetch)

# 返回上次抓取分析 robots.txt 时间
print(rp.mtime())

# 返回 robotx.txt 文件对抓取延迟限制的值
print(rp.crawl_delay('*'))
print(rp.crawl_delay('MSNBot'))
